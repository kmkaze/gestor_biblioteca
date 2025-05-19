class Usuario:
    def __init__(self, id, nombre, apellido, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.reservas = []  # Lista para almacenar los libros reservados

    def inicio_sesion(self, email, contraseña):
        return self.email == email and self.contraseña == contraseña

    def reservar_libro(self, libro):
        if libro.disponible:
            self.reservas.append(libro)
            libro.actualizar_disponibilidad(False)
            return f"Has reservado el libro '{libro.titulo}'"
        return f"El libro '{libro.titulo}' ya está reservado"

    def devolver_libro(self, titulo):
        libro_a_devolver = next((libro for libro in self.reservas if libro.titulo == titulo), None)
        if libro_a_devolver:
            self.reservas.remove(libro_a_devolver)
            libro_a_devolver.actualizar_disponibilidad(True)
            return f"Has devuelto el libro '{titulo}'"
        return f"No tienes el libro '{titulo}' reservado"

    def ver_reservas(self):
        if self.reservas:
            return [libro.mostrar_informacion() for libro in self.reservas]
        return "No tienes libros reservados"