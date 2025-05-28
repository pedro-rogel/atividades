from config import create_app
from app.controllers.atividade_controller import atividade_bp

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
