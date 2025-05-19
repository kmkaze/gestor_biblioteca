import Biblioteca
class Ejemplares:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def agregar_libro(self, biblioteca, libro):
        if isinstance(biblioteca, Biblioteca):  # Verificar tipo
            biblioteca.libros.append(libro)
            return f"Libro '{libro.titulo}' añadido a la biblioteca"
        return "Error: El objeto proporcionado no es una biblioteca válida"

    def eliminar_libro(self, biblioteca, libro):
        if isinstance(biblioteca, Biblioteca):  # Verificar tipo
            if libro in biblioteca.libros:
                biblioteca.libros.remove(libro)
                return f"Libro '{libro.titulo}' eliminado del sistema"
            return f"Error: El libro '{libro.titulo}' no está en la biblioteca"
        return "Error: El objeto proporcionado no es una biblioteca válida"