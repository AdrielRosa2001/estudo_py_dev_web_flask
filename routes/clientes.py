from  flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
    """Renderiza a lista de clientes"""
    pass

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Adiciona um novo cliente ao banco de dados """
    pass

@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    pass

@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    """ Renderiza o cliente através do id informado em url """
    pass

@cliente_route.route('/<int:cliente_id>/edit', methods=['PUT'])
def form_edit_cliente(cliente_id):
    """ Renderiza um formulário para editar os dados dos clientes """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    """ Deleta o cliente do banco de dados """
    pass