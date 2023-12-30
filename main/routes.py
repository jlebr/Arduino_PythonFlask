from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

main_bp = Blueprint('main', __name__, url_prefix='/main', template_folder='templates', static_folder='static')

# Ruta principal
@main_bp.route('', methods=['GET'])
def main():
    last_value = False
    return render_template('index.html', last_value=last_value)

# Obteniendo la respuesta del Front
@main_bp.route('', methods=['POST'])
def get_data():
    data = request.form['data']
    print(data)
    return redirect(url_for('main.main'))