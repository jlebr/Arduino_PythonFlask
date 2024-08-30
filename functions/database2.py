import sqlite3
from typing import Tuple

def init():
    # Conectar o crear la base de datos
    conexion = sqlite3.connect('estado2.db')
    # Obtener un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    # Crear la tabla Estado si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor BOOLEAN,
            fan TEXT(15)
        )
    ''')
    
    # Insertar una fila con id=1 si no existe
    cursor.execute('''
        INSERT OR IGNORE INTO Estado (id, valor, fan) VALUES (1, 0, "")
    ''')

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def get_status() -> Tuple[bool, str]:
    conexion = sqlite3.connect('estado2.db')
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT valor, fan FROM Estado WHERE id=1
    """)
    response = cursor.fetchone()
    conexion.close()

    if not response:
        return None, None
    else:
        return response[0], response[1]

def update_status(status:bool, new_text:str) -> bool:
    try:
        conexion = sqlite3.connect('estado2.db')
        cursor = conexion.cursor()
        cursor.execute(f'''
            UPDATE Estado SET valor="{status}", fan="{new_text}" WHERE id=1
        ''')
        conexion.commit()
        conexion.close()

        print(f"Valor Actualizado {status}, Nueva Cadena {new_text}")
        #return True
        return status, new_text
    
    except Exception as e:
        return False, f"Error: {e}"

if __name__ == '__main__':
    # Llamar a la función para inicializar la base de datos
    init()
    
    # Actualizar el estado y mostrar el resultado
    print("Vamos a cargar la data")
    update_status(True, "Texto jorge")
    
    # Obtener y mostrar el estado actualizado
    status, text = get_status()
    print(f"Estado Actual: {status}, Texto: {text}")

