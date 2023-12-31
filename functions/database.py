import sqlite3

def init():
    # Conectar o crear la base de datos
    conexion = sqlite3.connect('estado.db')
    # Obtener un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    # Crear la tabla Estado si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor BOOLEAN
        )
    ''')
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def get_status() -> bool:
    conexion = sqlite3.connect('estado.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT valor FROM Estado WHERE id=1')
    response = cursor.fetchone()
    conexion.close()

    return response[0]

def update_status(status:bool) -> bool:
    try:
        conexion = sqlite3.connect('estado.db')
        cursor = conexion.cursor()
        cursor.execute(f'UPDATE Estado SET valor="{status}" WHERE id=1')
        conexion.commit()
        conexion.close()

        print(f"Valor Actualizado {status}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    # Llamar a la función para inicializar la base de datos
    init()
    print(update_status(True))
    print(get_status())
