from app import db
from sqlalchemy.orm import relationship

class Atividade(db.Model):
    __tablename__ = "atividades"

    id_atividade = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, db.ForeignKey=(id_disciplina))
    enunciado = db.Column(db.String(50), nullable=False)


    respostas = relationship('Respostas', back_populates='atividade')



class Resposta(db.Model):
    __tablename__ = 'respostas'

    id = db.Column(db.Integer, primary_key=True)
    id_atividade = db.Column(db.Integer, db.ForeignKey('atividade_id'))
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno_id'))  # ou só 'alunos.id' se a tabela existir
    resposta = db.Column(db.String(100))
    nota = db.Column(db.Integer, nullable=True)

    atividade = relationship('Atividade', back_populates='respostas') 


class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return db.session.query(Atividade).all()

def obter_atividade(id_atividade):
    atividade = db.session.get(Atividade, id_atividade)
    if atividade:
        return atividade
    raise AtividadeNotFound()
