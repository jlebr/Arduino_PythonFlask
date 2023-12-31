try:
    from functions import database
except:
    import database

# Encendedor
def switch(value:str) -> bool:
    print(value)
    if value == 'encender':
        # Logica para encender el Led
        # Mostrar el estado anterior
        return database.update_status(True)
    
    if value == 'apagar':
        # Logica para apagar el Led
        # Mostrar el estado anterior
        return database.update_status(False)

    else:
        # Retornar el ultimo valor
        return database.get_status()

if __name__ == '__main__':
    print(switch('apagar'))