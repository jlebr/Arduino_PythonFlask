"""
En esta parte es donde se genera la logica de arduinio que va a encargarse de mandar los comandos para la parte de arduino_conect"""


try:
    from functions import database
    from functions import database2
    #from functions import arduino_conect_Original as arduino #Comento esta linea que al cambiar el archivo se renombro aquí
    from functions import arduino_conect as arduino
except:
    import database
    import database2
    #import functions.arduino_conect_Original as arduino  #Comento esta linea que al cambiar el archivo se renombro aquí
    import functions.arduino_conect as arduino


# Encendedor
def switch(value:str) -> bool:
    print(value)
    if value == 'encender':
        arduino.comunicate(1)
        Led = "ON"
        last_value = database.update_status(True)
        fan="NONE Encender"
        return last_value, Led, fan

    
    if value == 'apagar':
        arduino.comunicate(0)
        Led = "OFF"
        last_value = database.update_status(False)
        fan ="NONE Apagar"
        return last_value, Led, fan

    else:
        arduino.comunicate(2)
        last_value = database.get_status() 
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        fan="NONE Estado"
        return last_value, Led, fan
    
# Ventilador cooming soon
def switchVe(value:str) -> bool:
    print(value)
    if value == 'Vel 1':
        #arduino.comunicate(4)
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 1" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan

    if value == 'Vel 2':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 2" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan    
    
    if value == 'Vel 3':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 3" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan

    if value == 'Apagar':
        #arduino.comunicate(3)
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "OFF" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan

# Ventilador & Led
def switchAll(value:str) -> bool:
    print(value)
    # Parte del Ventilador
    if value == 'Vel 1':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 1" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan

    if value == 'Vel 2':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 2" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan    
    
    if value == 'Vel 3':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 3" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan

    if value == 'Apagar':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "OFF" # Variable de Ventilador apagado.
        last_value = database.get_status()
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        return last_value, Led, fan
    #Parte del Led
    if value == 'encender':
        arduino.comunicate(1)
        Led = "ON"
        last_value = database.update_status(True)
        fan="NONE Encender"
        return last_value, Led, fan

    
    if value == 'apagar':
        arduino.comunicate(0)
        Led = "OFF"
        last_value = database.update_status(False)
        fan ="NONE Apagar"
        return last_value, Led, fan

    else:
        arduino.comunicate(2)
        last_value = database.get_status() 
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        fan="NONE Estado"
        return last_value, Led, fan         
       
# Ventilador & Led 2 valores en la DB
def switchAll2DB(value:str) -> bool:
    print(value)
    # Parte del Ventilador
    if value == 'Vel 1':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        
        arduino.comunicate(4)
        valor, fan = database2.get_status()
        last_value = valor
        fan = "ON Vel 1" # Variable de Ventilador apagado.
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        last_value, fan = database2.update_status(last_value, fan)
        return last_value, Led, fan

    if value == 'Vel 2':
        #arduino.comunicate(10) # Voy a enviar el comando 00 que apagara el ventilador
        arduino.comunicate(5)
        valor, fan = database2.get_status()
        last_value  = valor
        fan = "ON Vel 2" # Variable de Ventilador apagado.
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        last_value, fan = database2.update_status(last_value, fan)
        return last_value, Led, fan    
    
    if value == 'Vel 3':
        #arduino.comunicate(11) # Voy a enviar el comando 00 que apagara el ventilador
        arduino.comunicate(6)
        valor, fan = database2.get_status()
        last_value = valor
        fan = "ON Vel 3" # Variable de Ventilador apagado.
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        last_value, fan = database2.update_status(last_value, fan)
        return last_value, Led, fan

    if value == 'Apagar':
        #arduino.comunicate(00) # Voy a enviar el comando 00 que apagara el ventilador
        arduino.comunicate(3)
        valor, fan = database2.get_status()
        last_value = valor
        fan = "OFF" # Variable de Ventilador apagado.
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        valor, fan = database2.update_status(last_value, fan)
        print(f'Fan: {fan}, Last Value: {last_value}, Led: {Led}')
        return last_value, Led, fan

    #Parte del Led
    if value == 'encender':
        arduino.comunicate(1)
        valor, fan = database2.get_status() 
        Led = "ON"
        last_value = True
        valor, fan = database2.update_status(True, fan)
        #fan="NONE Encender"
        return last_value, Led, fan

    
    if value == 'apagar':
        arduino.comunicate(0)
        valor, fan = database2.get_status() 
        Led = "OFF"
        last_value = False
        valor, fan = database2.update_status(False, fan)
        #fan ="NONE Apagar"
        return last_value, Led, fan

    else:
        arduino.comunicate(2)
        valor, fan = database2.get_status() 
        last_value = valor
        if last_value =="True":
            Led = "ON"
        else:
            Led = "OFF"
        
        return last_value, Led, fan

if __name__ == '__main__':
    print(switch('apagar'))