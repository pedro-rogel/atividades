from flask import Blueprint, jsonify, request
from app.model.atividade_model import Atividade, obter_atividade_id, AtividadeNotFound
from app.clients.pessoa_service_client import PessoaServiceClient
from app import db
import requests

routes = Blueprint("routes", __name__)

@routes.route('/', methods=['GET'])
def listar_atividades():
    try:
        atividades = Atividade.query.all()
        return jsonify([
            {
                "id_atividade" : r.id,
                "id_disciplina": r.id_disciplina,
                "enunciado" : r.enunciado
            } for r in atividades
        ])
    except AtividadeNotFound:
        return jsonify({"erro": "Nao há atividades"})



@routes.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = obter_atividade_id(id_atividade)
        print(atividade)
        payload = {
            "id_atividade":  atividade.id,
            "id_disciplina": atividade.id_disciplina,
            "enunciado":     atividade.enunciado,
        }
        return jsonify({"data": payload})
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@routes.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = obter_atividade_id(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    

@routes.route('/', methods=['POST'])
def criar_atividade():
    dados = request.json
    atividade = Atividade(
        id=dados.get('id'),
        id_disciplina=dados.get("id_disciplina"),
        enunciado=dados.get("enunciado")
        
    )
    
    db.session.add(atividade)
    db.session.commit()
    
    return jsonify({"message": "Atividade criada com sucesso"})


@routes.route('/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade):
        atividade = obter_atividade_id(id_atividade)
        if not atividade:  
            return jsonify({"erro": "Atividade não encontrada"})
        db.session.delete(atividade)
        db.session.commit()
        
        return jsonify({'message': 'Atividade deletada com sucesso'}), 200