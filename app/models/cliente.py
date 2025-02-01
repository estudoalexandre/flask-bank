from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UniqueConstraint
class Cliente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    contas = db.relationship('Conta', back_populates='cliente', cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('cpf', name='uq_cliente_cpf'),  # Define um nome para a constraint
    )

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)
    
    def __repr__(self):
        return f'<Cliente {self.nome} - CPF: {self.cpf}>'