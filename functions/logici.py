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

    if value == 'Vel 1':
        #arduino.comunicate(01) # Voy a enviar el comando 00 que apagara el ventilador
        fan = "ON Vel 1" # Variable de Ventilador apagado.
        last_value = database.get_status()#"33" #database.update_status(True)
        return last_value, fan
    
    else:
        
        return 

if __name__ == '__main__':
    print(switch('apagar'))