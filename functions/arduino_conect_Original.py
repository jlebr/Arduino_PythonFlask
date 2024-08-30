import serial
import time

#puerto_serial = 'COM4'
def comunicate(value:int) -> bool:
    """
    value: 0 -> apagado 1 -> Encendido
    """
    #puerto_serial = '/dev/ttyUSB0'  # Cambia esto por tu puerto serial específico
    puerto_serial = 'COM4'

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

def leer_serial():

    #puerto_serial = '/dev/ttyUSB0'  # Cambia esto por tu puerto serial específico
    puerto_serial = 'COM4'
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

if __name__ == '__main__':
    print(comunicate(1))

"""
NOTA: POR ALGUN MOTIVO ESTE ARCHIVO EN WINDOWS NO ME FUNCIONA Y NO DEJA QUE ME TRABAJE BIEN EL ARDUINO.
"""