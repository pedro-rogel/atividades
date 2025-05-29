import requests 
from app import db
from app.models.disciplina_model import DisciplinaNaoEncontrada, Disciplina
BASE_URL = 'https://school-system-hfwh.onrender.com'

professores = requests.get(f"{BASE_URL}/professores").json()
alunos = requests.get(f"{BASE_URL}/alunos").json()

def listar_professores():
    return professores

def listar_alunos():
    return alunos

def leciona(id_professor, id_disciplina):
    """Verifica se um professor leciona uma disciplina específica."""
    for disciplina in Disciplina.query.all():
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada
