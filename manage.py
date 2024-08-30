from flask_cors import CORS
from flask import Flask 
from flask import redirect
from flask import url_for

import os 

from main.routes import main_bp

# Configuración Inicial de la APP
app = Flask(__name__)
CORS(app)

# Redireccionamos a la ruta main
@app.route('/')
def home():
    return redirect(url_for('main.main'))

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(
        debug=False,
        host="0.0.0.0",
        port=5000
    )