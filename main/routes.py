from flask import Blueprint
from flask import render_template

main_bp = Blueprint('main', __name__, url_prefix='/main', template_folder='templates', static_folder='static')

# Ruta principal
@main_bp.route('', methods=['GET'])
def main():
    return render_template('index.html')