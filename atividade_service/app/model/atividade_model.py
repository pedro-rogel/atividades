from app import db


class Atividade(db.Model):
    __tablename__ = "atividades"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(50), nullable=False)
    



class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return db.session.query(Atividade).all()

def obter_atividade_id(id_atividade):
    atividade = db.session.get(Atividade, id_atividade)
    if atividade:
        return atividade
    raise AtividadeNotFound()
