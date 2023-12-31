try:
    from functions import database
    from functions import arduino_conect as arduino
except:
    import database
    import arduino_conect as arduino

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
        return database.get_status()

if __name__ == '__main__':
    print(switch('apagar'))