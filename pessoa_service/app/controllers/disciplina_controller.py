# app/controllers/disciplina_controller.py
from flask import Blueprint, jsonify, request, current_app
from app.models.disciplina_model import Disciplina
from app import db
import requests

routes_dc = Blueprint("disciplina", __name__, url_prefix="/disciplinas")

def fetch_alunos():
    base = current_app.config.get(
        "PESSOA_SERVICE_URL",
        "https://school-system-hfwh.onrender.com"
    )
    resp = requests.get(f"{base}/alunos")
    resp.raise_for_status()
    return resp.json()

def fetch_professores():
    base = current_app.config.get(
        "PESSOA_SERVICE_URL",
        "https://school-system-hfwh.onrender.com"
    )
    resp = requests.get(f"{base}/professores")
    resp.raise_for_status()
    print(resp.json())
    return resp.json()

@routes_dc.route("/", methods=["GET"])
def listar_disciplinas():
    disciplinas = Disciplina.query.all()
    return jsonify([d.to_dict() for d in disciplinas])

@routes_dc.route("/", methods=["POST"])
def criar_disciplina():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    if not nome:
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    publica        = dados.get("publica", False)
    alunos_ids     = dados.get("alunos", fetch_alunos())
    professores_ids = dados.get("professores", [])

    # agora sim, dentro do context, podemos usar fetch_*
    try:
        valid_alunos = {a["id"] for a in fetch_alunos()}
    except requests.HTTPError as e:
        return jsonify({"erro": f"Falha ao buscar alunos: {e}"}), 502

    invalid_alunos = [i for i in alunos_ids if i not in valid_alunos]
    if invalid_alunos:
        return jsonify({"erro": f"IDs de alunos inválidos: {invalid_alunos}"}), 400

    try:
        valid_profs = {p["id"] for p in fetch_professores()}
    except requests.HTTPError as e:
        return jsonify({"erro": f"Falha ao buscar professores: {e}"}), 502

    invalid_profs = [i for i in professores_ids if i not in valid_profs]
    if invalid_profs:
        return jsonify({"erro": f"IDs de professores inválidos: {invalid_profs}"}), 400

    disc = Disciplina(
        nome=nome,
        publica=publica,
        alunos=alunos_ids,
        professores=professores_ids
    )
    db.session.add(disc)
    db.session.commit()

    return jsonify({"data": disc.to_dict()}), 201
