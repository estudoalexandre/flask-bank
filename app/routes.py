from flask import Flask, render_template, Blueprint, redirect, url_for, request
from app.models import Cliente
from app import db
from app.services import criar_cliente
from flask_login import login_user, login_required, logout_user


bp = Blueprint('main', __name__)



@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']
        cliente = criar_cliente(nome, cpf, email, senha)
        login_user(cliente)
        return redirect(url_for('main.index'))
    return render_template('cadastrar.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return "Login"