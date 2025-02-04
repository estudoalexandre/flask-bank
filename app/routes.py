from flask import Flask, render_template, Blueprint, redirect, url_for, request, flash
from app.models import Cliente, Conta
from app import db
from app.services import criar_cliente, buscar_cliente_por_cpf
from flask_login import login_user, login_required, logout_user, current_user


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
        return redirect(url_for('main.login'))
    return render_template('cadastrar.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['password']
        user = Cliente.query.filter_by(email=email).first()
        
        if user and user.check_senha(senha):
            print("Senha válida, tentando logar...")
            login_user(user)
            print(f"Usuário logado: {current_user}")
            return redirect(url_for('main.dashboard'))
        else:
            print()
            flash('Email ou senha inválidos', 'danger')
    
    return render_template('login.html')

@bp.route('/index')
@login_required
def dashboard():
    return render_template('index.html')

@bp.route('/depositar', methods=['GET', 'POST'])
def depositar():
    conta = Conta.query.filter_by(cliente_id=current_user.id).first()
    if request.method == 'POST':
        saldo = float(request.form['saldo'])
        print(f"Aqui é o tipo: {type(saldo)}")
        conta.saldo += saldo
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('depositar.html')

@bp.route('/transferir', methods=['GET', 'POST'])
def transferir():
    conta = Conta.query.filter_by(cliente_id=current_user.id).first()
    if request.method == 'POST':
        saldo = float(request.form['saldo'])
        cpf = request.form['cpf']
        conta_destino = buscar_cliente_por_cpf(cpf)
        if conta_destino:
            conta.saldo -= saldo
            conta_destino.saldo += saldo
            db.session.commit()
            return redirect(url_for('main.dashboard'))
        else:
            flash('CPF inválido', 'danger')
    return render_template('transferir.html')