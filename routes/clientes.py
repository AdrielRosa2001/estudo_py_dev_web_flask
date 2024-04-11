from  flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
    """Renderiza a lista de clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Adiciona um novo cliente ao banco de dados """
    data = request.json
    novo_usuario = {
        "id": CLIENTES[len(CLIENTES)-1]['id']+1,
        "nome": data['nome'],
        "email": data['email']
    }
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Renderiza o cliente através do id informado em url """
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Renderiza um formulário para editar os dados dos clientes """
    cliente = None
    for c in CLIENTES:
        if c['id'] ==  cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualiza cliente no banco """
    cliente_editado = None
    data = request.json
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    """ Deleta o cliente do banco de dados """
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {"deleted": "ok"}