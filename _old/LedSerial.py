"""
Se requie tener Python en la pc instaldo y la libreria serial & time
Este codigo sirve para hacer las prueba de envio e comando al arduino por puerto serial
mediante el uso de funciones separadas.
"""

import serial, time
#arduino = serial.Serial('COM4',9600)
#time.sleep(2)

def encender(valor):
    print (valor)
    arduino = serial.Serial('COM4',9600)
    time.sleep(2)
    arduino.write(b'1')
    arduino.close()

def apagar(valor):
    print(valor)
    arduino = serial.Serial('COM4',9600)
    time.sleep(2)
    arduino.write(b'0')
    arduino.close()

def estado(valor):
    print(valor)
    arduino = serial.Serial('COM4',9600)
    time.sleep(2)
    arduino.write(b'0')
    print(arduino.readline())
    arduino.close()

#Esta liena llama a la funcion apagar y le pasa el valor 0
#apagar(0) 
#time.sleep(10) #Tiempo de retardo 10 

#Esta liena llama a la funcion encender y le pasa el valor 1
#encender(1) 
#time.sleep(10) #Tiempo de retardo 10 

#Esta liena llama a la funcion estado y le pasa el valor 2
#estado(2) 

# Realizado por Jorge Barboza