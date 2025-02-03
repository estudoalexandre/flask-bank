from app import db
from app.models.cliente import Cliente

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150), nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    agencia = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(150), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    cliente = db.relationship('Cliente', back_populates='contas')

    def __repr__(self):
        return f'<Conta {self.tipo} - Agencia {self.agencia} - Numero {self.numero}>'