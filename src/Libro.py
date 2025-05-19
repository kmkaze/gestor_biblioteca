class Libro:
    def __init__(self, id, titulo, autor, isbn, editorial, año, disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.año = año
        self.disponible = disponible  # 🔹 Ahora acepta disponible como argumento

    def mostrar_informacion(self):
        return (f"Titulo: {self.titulo} | Autor: {self.autor} | Año: {self.año} | "
                f"ISBN: {self.isbn} | Editorial: {self.editorial} | Estado: {'Disponible' if self.disponible else 'No Disponible'}")

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "Disponible" if disponible else "Reservado"
        return f"El libro '{self.titulo}' ahora está {estado}"
    
    
    def __str__(self):
        return self.mostrar_informacion()