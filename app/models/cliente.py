from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Cliente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    contas = db.relationship('Conta', back_populates='cliente', cascade='all, delete-orphan')

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)
    
    def __repr__(self):
        return f'<Cliente {self.nome}>'