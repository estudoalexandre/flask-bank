from app import db
from sqlalchemy import event
from app.models import Cliente, Conta
import random


def gerar_conta(cliente):
    agencia = random.randint(2800, 2899)
    digito = random.randint(0, 9)
    numero = f"{random.randint(10000, 99999)} - {digito}"
    saldo = 0.0
    tipo = 'Conta Corrente'
    conta = Conta(tipo=tipo, saldo=saldo, agencia=agencia, numero=numero, cliente_id=cliente.id)
    db.session.add(conta)
    
    return

@event.listens_for(Cliente, 'after_insert')
def criar_conta_pos_cadastro(mapper, connection, target):
    gerar_conta(target)