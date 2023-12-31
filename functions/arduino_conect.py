import serial
import time

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
        time.sleep(1)
        return True

    except Exception as e:
        print("Error al establecer la conexión:", e)
        return False

if __name__ == '__main__':
    print(comunicate(1))