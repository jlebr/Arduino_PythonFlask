from flask import Flask, render_template
import serial, time

app = Flask(__name__)
arduino = serial.Serial('COM4', 9600)  # Reemplaza 'COM3' con el puerto serial de tu Arduino
time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encender', methods=['GET'])
def encender_led():
    arduino.write(b'H')  # Envía 'H' para encender el LED
    return 'LED encendido'

@app.route('/apagar', methods=['GET'])
def apagar_led():
    arduino.write(b'L')  # Envía 'L' para apagar el LED
    return 'LED apagado'

if __name__ == '__main__':
    app.run(debug=True)
