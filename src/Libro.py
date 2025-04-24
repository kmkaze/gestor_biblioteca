class Libro:
    def __init__(self, titulo, autor, isbn, editorial, año):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.año = año
        self.disponible = True  
    
    def mostrar_informacion(self):
        return f"Titulo: {self.titulo} Autor: {self.autor} Año: {self.año}"
    
    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        return f"El libro {self.titulo} - Estado {estado}"