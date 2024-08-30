from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from functions import logic
from functions import database
from functions import database2

main_bp = Blueprint('main', __name__, url_prefix='/main', template_folder='templates', static_folder='static')

# Ruta principal
@main_bp.route('', methods=['GET'])
def main():
    valor, fan = database2.get_status()
    last_value = valor
    #print("Valor 1: ", last_values)
    print("Valor 2 ", valor)
    print("Valor 3: ", fan)
    if last_value =="True":
        Led = "ON"
    if last_value =="False":
        Led = "OFF"
    else:
        print("NA")
    #fan="NONE MAIN"
    
    return render_template('index.html', last_value=last_value, Led=Led, fan=fan)

# Obteniendo la respuesta del Front
@main_bp.route('', methods=['POST'])
def get_data():
    data = request.form['data']
    #last_value, Led, fan = logic.switch(data) # Para el Led
    #last_value, Led, fan = logic.switchVe(data) # Para el ventilador
    #last_value, Led, fan = logic.switchAll(data) # Para Led & Ventilador
    last_value, Led, fan = logic.switchAll2DB(data) # Para Led & Ventilador
    return render_template('index.html', last_value=last_value, Led=Led, fan=fan)