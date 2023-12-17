"""
Se requie tener Python en la pc instaldo y la libreria serial
Este codigo sirve para enviar cualquier comando por serial al arduino
A su vez permite obtener la respuesta que nos envia el arduino y devolverla
cuando sea llamada la funcion desde otro script

Se tiene el escripts ==> SerialPersistente para probar esta logica
"""

import serial, time # Importo serial para poder comunicarme con el arduino

arduino = serial.Serial('COM4',9600) # Inicio conexion serial y a su vez configuro puerto y velocidad de comunicación con el arduino
time.sleep(10)

def mensajes(mensaje): # Funcion que recibe el parametro mensaje y le envia por serial al arduino
    if mensaje =="cerrar":
        arduino.close() #Cierro coenexion ene el arduino cuando se cumple que el mesnaje es igual a cerrar
        return("Se cierra conexion serial...")
    else:
        #arduino = serial.Serial('COM4',9600) # Inicio conexion serial y a su vez configuro puerto y velocidad de comunicación con el arduino
        #time.sleep(1)
        arduino.write(mensaje.encode()) # Envio el mensaje al arduino y lo codifico para que el arduino pueda interpretar la información.
        return(arduino.readline().decode().rstrip('\n')) # Recibo la respuesta del arduino la codifico a un formato que me permita ser leida en formato texto.
    
def iniciar(serial):
    if serial=="serial":
       arduino = serial.Serial('COM4',9600) # Inicio conexion serial y a su vez configuro puerto y velocidad de comunicación con el arduino