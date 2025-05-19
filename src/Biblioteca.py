import sqlite3
from src.Usuario import Usuario
from src.Libro import Libro

class Biblioteca:
    def __init__(self, db_path="biblioteca.db"):
        self.db_path = db_path

        self.usuarios = self.cargar_usuarios()
        self.libros = self.cargar_libros()

    def buscar_usuario(self, email):
        return next((usuario for usuario in self.usuarios if usuario.email == email), None)
    
    def registrar_usuario(self, usuario):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios (nombre, apellido, email, contraseña) VALUES (?, ?, ?, ?)",
                    (usuario.nombre, usuario.apellido, usuario.email, usuario.contraseña))

        conn.commit()
        conn.close()

        self.usuarios = self.cargar_usuarios()  # 🔹 Carga los usuarios nuevamente
        return f"Usuario '{usuario.nombre} {usuario.apellido}' registrado correctamente"
    
    def eliminar_usuario(self, email):
        import sqlite3
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            email_proc = email.strip().lower()
            cursor.execute("DELETE FROM usuarios WHERE LOWER(email) = ?", (email_proc,))
            conn.commit()
            print("Rowcount eliminación usuario:", cursor.rowcount)  
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al eliminar usuario:", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def cargar_usuarios(self):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        usuarios_db = cursor.fetchall()

        conn.close()

        return [Usuario(id, nombre, apellido, email, contraseña) for id, nombre, apellido, email, contraseña in usuarios_db]
    
    def registrar_libro(self, libro):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO libros (titulo, autor, isbn, editorial, año, disponible) VALUES (?, ?, ?, ?, ?, ?)",
                    (libro.titulo, libro.autor, libro.isbn, libro.editorial, libro.año, libro.disponible))

        conn.commit()
        conn.close()

        self.libros = self.cargar_libros()  
        return f"Libro '{libro.titulo}' registrado correctamente"

    def cargar_libros(self):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM libros")
        libros_db = cursor.fetchall()

        conn.close()

        return [Libro(id, titulo, autor, isbn, editorial, año, disponible) for id, titulo, autor, isbn, editorial, año, disponible in libros_db]

    def eliminar_libro(self, titulo):
            import sqlite3
            conn = None
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                titulo_proc = titulo.strip().lower()
                cursor.execute("DELETE FROM libros WHERE LOWER(titulo) = ?", (titulo_proc,))
                conn.commit()
                print("Rowcount eliminacion:", cursor.rowcount)
                return cursor.rowcount > 0
            except Exception as e:
                print("Error al eliminar libro:", e)
                return False
            finally:
                if conn is not None:
                    conn.close()

    
    def ver_libros(self):
        if not self.libros:
            return "No hay libros disponibles en la biblioteca."

        resultado = "Lista de libros:\n"
        for libro in self.libros:
            resultado += f"- {libro.titulo} de {libro.autor} (ISBN: {libro.isbn})\n"

        return resultado