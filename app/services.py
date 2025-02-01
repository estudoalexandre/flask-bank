from app.models.cliente import Cliente
from app.models.conta import Conta
from app import db


def criar_cliente(nome, cpf, email, senha):
    cliente = Cliente(nome=nome, cpf=cpf, email=email, senha=senha)
    db.session.add(cliente)
    db.session.commit()
    return cliente

