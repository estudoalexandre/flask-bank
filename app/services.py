from app.models.cliente import Cliente
from app.models.conta import Conta
from app import db


    
    

def criar_cliente(nome, cpf, email, senha):
    cliente = Cliente(nome=nome, cpf=cpf, email=email)
    cliente.set_senha(senha)
    db.session.add(cliente)
    db.session.commit()
    return cliente

def buscar_cliente_por_cpf(cpf):
    return Conta.query.join(Cliente).filter(Cliente.cpf == cpf).first()

