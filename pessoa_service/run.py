from config import Config
from flask import Flask
from app import db
from app.controllers.pessoa_controller import routes_pc
from app.controllers.disciplina_controller import routes_dc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///disciplinas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(routes_pc, url_prefix='/pessoas')
app.register_blueprint(routes_dc, url_prefix='/disciplinas')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)

