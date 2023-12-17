"""
Se requie tener Python en la pc
Se importa de LedSerial_V2 para poder enviar comandos al arduino y así probar la funcionalidad del mismo
"""
from LedSerial_V2 import mensajes
"""
while True:
    mensaje = input("Ingresa el mensaje: ")
    if mensaje == "cerrar":
        print("Se procede a cerrar la conexion Serial de arduino")
        mensajes(mensaje)
        print(mensajes(mensaje))
        break
    mensajes(mensaje)
    print(mensajes(mensaje))
"""


def enviar(mensaje):
    if mensaje == "cerrar":
        print("Se procede a cerrar la conexion Serial de arduino")
        mensajes(mensaje)
        print(mensajes(mensaje))
    
    mensajes(mensaje)
    print(mensajes(mensaje))




enviar("1")