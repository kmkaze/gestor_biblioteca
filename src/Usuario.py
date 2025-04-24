class Usuario:
    def __init__(self, id_cliente, nombre, apellido, email, contraseña):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.reservas = []

    def inicio_sesion(self, email, contraseña):
        return self.email == email and self.contraseña == contraseña
    
    def nueva_reserva(self, libro):
        if libro.disponible:
            self.reservas.append(libro)
            libro.actualizar_disponibilidad(False)
            return f"Libro {libro.titulo} prestado"
        else:
            return f"Libro no disponible"
    
    def devolver_libro(self, libro):
        if libro in self.reservas:
            self.reservas.remove(libro)
            libro.actualizar_disponibilidad(True)
            return f"Libro {libro.titulo} devuelto"
        else:
            return f"El libro {libro.titulo} no está en las reservas."
    
    def ver_reservas(self):
        return [libro.titulo for libro in self.reservas]


