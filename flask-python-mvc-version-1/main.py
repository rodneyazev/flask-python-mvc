from flask import Flask, render_template, request, redirect, session, flash


class Jogos:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


lista_de_jogos_1 = Jogos('Resident Evil', 'Horror', 'Xbox One S')
lista_de_jogos_2 = Jogos('Red Dead Redemption 2', 'Open World', 'PC')
lista_de_jogos_3 = Jogos('Mortal Kombat 1', 'Fight', 'Playstation 5')
lista_de_jogos = [lista_de_jogos_1, lista_de_jogos_2, lista_de_jogos_3]

app = Flask(__name__)

app.secret_key = 'rodney'


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login?proxima=formulario')
    return render_template('lista.html', titulo='Jogos', lista_de_jogos=lista_de_jogos)


@app.route('/formulario')
def formulario():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login?proxima=formulario')
    return render_template('formulario.html', titulo='Cadastro - Novo jogo')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect('/login')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect('/')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'aloha' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + " logado com sucesso.")
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário ou senha inválidos.')
        return redirect('/login')


app.run(debug=True)







"""
@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'aloha' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + " logado com sucesso.")
        return redirect('/formulario')
    else:
        flash('Usuário ou senha inválidos.')
        return redirect('/login')
"""