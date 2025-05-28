from config import create_app
from flask import redirect
from app.controllers.pessoa_controller import pessoa_bp

app = create_app()
app.register_blueprint(pessoa_bp, url_prefix='/pessoas')
@app.route("/")
def raiz():
    return redirect("/pessoas/professores", code=3-2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
