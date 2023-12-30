"""
Se requie tener Python en la pc instaldo y la libreria serial
Este codigo sirve para hacer las prueba de envio e comando al arduino por puerto serial
"""

import serial, time
arduino = serial.Serial('COM4',9600) #Aqui se configura el puerto y la velocidad de comunicación con el arduino por serial, tambien inicia el puerto serial.
time.sleep(2) #Detiene el codigo por 2 ms

#Envia al aduido un comando 1 para encender el LED
arduino.write(b'1')
print("Se ha enviado el comando encender")
respuesta = arduino.readline()
print("Respuesta ==> " ,respuesta.decode().rstrip('\n'))


time.sleep(5) #Detiene el codifo 5 ms

#Envia al arduino el comando 0 para apagar el LED
arduino.write(b'0')
print("Se ha enviado el comando apagar")
respuesta = arduino.readline()
print("Respuesta ==> " ,respuesta.decode().rstrip('\n'))

time.sleep(5) #Detiene el codifo 5 m

#Envia al arduino el comando 2 para saber el estado del
arduino.write(b'2')
print("Se ha enviado el comando estado")
respuesta = arduino.readline()
print("Respuesta ==> " ,respuesta.decode().rstrip('\n'))

arduino.close() #Aqui cerramos comunicación serial con el arduino.

# Realizado por Jorge Barboza