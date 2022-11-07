from flask import Flask
from extensions import db

class Agenda(db.Model):
    __tablename__ = "agenda"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    empresa = db.Column(db.String(150))
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(150))

    def init(self, id, nome, empresa, email, telefone):
        self.id = id;
        self.nome = nome
        self.empresa = empresa
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return "<Agenda(id={}, nome={}, empresa={}, telefone={}, email={})>".format(self.id, self.nome, self.empresa, self.telefone, self.email)