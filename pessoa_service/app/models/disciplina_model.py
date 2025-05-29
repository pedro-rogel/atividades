from app import db
import requests

BASE_URL = 'https://school-system-hfwh.onrender.com'

professores = requests.get(f"{BASE_URL}/professores").json()
alunos = requests.get(f"{BASE_URL}/alunos").json()

class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id           = db.Column(db.Integer, primary_key=True)
    nome         = db.Column(db.String(100), nullable=False)
    publica      = db.Column(db.Boolean,   default=False, nullable=False)
    alunos       = db.Column(db.JSON,   nullable=False, default=list)
    professores = db.Column(db.JSON,    nullable=False, default=list)

    def to_dict(self):
        return {
            "id":           self.id,
            "nome":         self.nome,
            "publica":      self.publica,
            "alunos":       self.alunos,
            "professores":  self.professores,
        }

class DisciplinaNaoEncontrada(Exception):
    pass