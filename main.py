from flask import Flask, url_for, render_template
#Inicialização Inicio
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Adriel", "membro_ativo": True},
        {"nome": "Carlos", "membro_ativo": False},
        {"nome": "Renato", "membro_ativo": False},
        {"nome": "Roberio", "membro_ativo": False}
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def sobre():
    return f"""
    <h1>Página Sobre</h1>
    <b>Olá galera</b>
    <a href='{url_for('ola_mundo')}'>Voltar ao inicio</a>
"""

# Execução final
app.run(debug=True)