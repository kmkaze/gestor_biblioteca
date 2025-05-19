import sqlite3
from getpass import getpass

def cambiar_contrasena(db_path, email, nueva_contrasena):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE usuarios SET contraseña = ? WHERE email = ?", (nueva_contrasena, email))
        conn.commit()
        
        if cursor.rowcount == 0:
            print("No se encontró un usuario con ese email.")
        else:
            print("Contraseña actualizada correctamente.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    db_path = 'biblioteca.db'  
    email = input("Ingresa el email del usuario: ")
    nueva_contrasena = getpass("Ingresa la nueva contraseña: ")
    confirmar_contrasena = getpass("Confirma la nueva contraseña: ")
    
    if nueva_contrasena != confirmar_contrasena:
        print("Las contraseñas no coinciden. Intenta nuevamente.")
    else:
        cambiar_contrasena(db_path, email, nueva_contrasena)