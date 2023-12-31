# Arduino y Flask

Este proyecto fue Realizaodo con Flask, y BluePrint para las rutas, ademas esta preparado para usar CORS

# Instrucciones de Uso
```bash
pip install -r requirements.txt

python manage.py
```

Cambiar en el archivo `arduino_conect.py` el puerto donde esta conectado el Arduino

# > Estructura del proyecto
## Arduino
Codigo para el Arduino 

## Functions
### `arduino_conect.py`
Esta función es la que envia el mensaje por serial al Arduino
```python
def comunicate(value:int) -> bool:
    """
    value: 0 -> apagado 1 -> Encendido
    """
    puerto_serial = '/dev/ttyUSB0'  # Cambia esto por tu puerto serial específico

    try:
        conexion = serial.Serial(puerto_serial, 9600, timeout=1)
        print("Conexión establecida correctamente")

        value = str(value)
        conexion.write(value.encode())
        print(f'Valor: {value}')
        conexion.close()
        return leer_serial()

    except Exception as e:
        print("Error al establecer la conexión:", e)
        return False
```

Esta función evita que la conexión se cierre y así poder mantener la conexión
```python
def leer_serial():

    puerto_serial = '/dev/ttyUSB0'  # Cambia esto por tu puerto serial específico

    try:
        conexion_serial = serial.Serial(puerto_serial, 9600, timeout=1)
        print("Conexión establecida correctamente")

        while True:
            # Leer datos desde el puerto serie
            datos = conexion_serial.readline().decode().strip()  # Lee una línea de datos

            if datos:
                print(f"Dato recibido por serial: {datos}")

    except serial.SerialException as e:
        print("Error al establecer la conexión:", e)
```

### `logic.py`
El modulo lo que hace es recibe los datos del formulario y realiza las diferentes acciones
```python
def switch(value:str) -> bool:
    print(value)
    if value == 'encender':
        arduino.comunicate(1)
        return database.update_status(True)

    
    if value == 'apagar':
        arduino.comunicate(0)
        return database.update_status(False)

    else:
        arduino.comunicate(2)
        return database.get_status()
```

### `databases`
Este modulo, crea, lee y actualiza los valores, para que no guardes los estados en texto plano

## main
### `routes`
Aqui esta la ruta main, esta ruta es la única y por ende la principal

```python
# Ruta principal
@main_bp.route('', methods=['GET'])
def main():
    last_value = database.get_status()
    return render_template('index.html', last_value=last_value)

# Obteniendo la respuesta del Front
@main_bp.route('', methods=['POST'])
def get_data():
    data = request.form['data']
    last_value = logic.switch(data)
    return render_template('index.html', last_value=last_value)


```
