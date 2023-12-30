"""
Este codigo tiene la funcion que levanta una pagina WEB en la cual se pueden mandar comando al arduino para encender, apagar y saber el estado de una salida.
esta construido con el framework Flask
a su vez usa el codigo LedSerial.py para hacer la comunicación con el arduino.
"""
#Pagina que se abre es:
# http://127.0.0.1:5000
# http://localhost:5000/
#===================================================================
#Librerias usadas para la pagian WEB
from flask import Flask, render_template
from flask import Flask, request
from flask_cors import CORS
from LedSerial import encender,apagar

#===================================================================
#Codigo que ejecuta la aplicación Flask
app = Flask(__name__)
# Ruta en la cual se puede guardar la data del arduino en un archivo last_value.txt
# ruta = "C:/Users/jlebr/Documents/Jorge Python Telegram/Codigo de prueba/ArduinoPython/LedSerialHttp V1/last_value.txt"
ruta = "last_value.txt"

#Route que recibe peticiones POST y la procesa para enviar lo que se quiere que el arduino haga.
@app.route('/request', methods=['POST'])
def handle_request():
    data = request.form['data']
    if data == 'encender': #Para valor recibido encender se ejecuta este codigo guarda dato, abre el txt y escribe el valor ON
        print(data)
        a = "ON"
        with open(ruta, 'w') as f:
            f.write(a)
            f.close()

        with open(ruta, 'r') as f:
            last_value = f.read()
        print ("ultimo valor es: "+last_value)
        encender(1) #lla a la funcion encender y le pasa el valor 1

        return render_template('index.html', last_value=last_value) #Va a retorna la pagina WEB con el valor actualizado
   
    elif data == 'apagar': #Para valor recibido apagar se ejecuta este codigo guarda dato, abre el txt y escribe el valor OFF
        print(data)
        print(data)
        a = "OFF"
        with open(ruta, 'w') as f:
            f.write(a)
            f.close()

        with open(ruta, 'r') as f:
            last_value = f.read()
        print ("ultimo valor es: "+last_value)
        apagar(0) #lla a la funcion apagar y le pasa el valor 0      
        return render_template('index.html', last_value=last_value) #Va a retorna la pagina WEB con el valor actualizado
   
   
    elif data == 'estado': #Para valor recibido estado se ejecuta este codigo abre el txt last_value.txt lee el valo y lo regresa
        print(data)
        print(data)
        with open(ruta, 'r') as f:
            last_value = f.read()

        print ("ultimo valor es: "+last_value)

        return render_template('index.html', last_value=last_value) #Va a retorna la pagina WEB con el valor actual del led
   
#Esta parte es donde se inica todo el codigo 
@app.route('/')
def index():
    with open(ruta, 'r') as f:
        last_value = f.read()
        print ("ultimo valor es: "+last_value)
    return render_template('index.html', last_value=last_value)
print("hola mundo")


if __name__ == '__main__':
    app.run(debug = True)

# Realizado por Jorge Barboza