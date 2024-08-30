"""
En esta parte es donde se genera la logica de arduinio que va a encargarse de mandar los comandos para la parte de arduino_conect"""


try:
    from functions import database
    #from functions import arduino_conect_Original as arduino #Comento esta linea que al cambiar el archivo se renombro aquí
    from functions import arduino_conect as arduino
except:
    import database
    #import functions.arduino_conect_Original as arduino  #Comento esta linea que al cambiar el archivo se renombro aquí
    import functions.arduino_conect as arduino


# Encendedor
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

if __name__ == '__main__':
    print(switch('apagar'))