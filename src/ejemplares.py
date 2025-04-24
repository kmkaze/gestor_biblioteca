class ejemplares:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def agregar_libro(self, biblioteca, libro):
        biblioteca.libros.append(libro)
        return f"Libro {libro.titulo} añadido"
        
    def eliminar_libro(self, biblioteca, libro):
        if libro in biblioteca.libros:
            biblioteca.libros.remove(libro)
            return f"Libro {libro.titulo} eliminado del sistema"