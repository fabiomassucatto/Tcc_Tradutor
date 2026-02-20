from flask import Blueprint, render_template, request, redirect, url_for
from db import mysql
from werkzeug.security import generate_password_hash, check_password_hash


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario and check_password_hash(usuario[3], senha):
            return "Login realizado com sucesso!"
        else:
            return "Email ou senha inválidos"

    return render_template('login.html')


@views.route('/cadastro', methods=['GET', 'POST'])

def cadastro():
   if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        senha_hash = generate_password_hash(senha)

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
            (nome, email, senha_hash)
        )
        mysql.connection.commit()
        cursor.close()

        return "Usuário cadastrado com sucesso!"

   return render_template('cadastro.html')
