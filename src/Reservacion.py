from datetime import datetime

class Reservacion:
    def __init__(self, id_reserva, libro, cliente, fechaPrestamo, fechaEntrega):
        self.id_reserva = id_reserva
        self.libro = libro  
        self.cliente = cliente  
        self.fechaPrestamo = fechaPrestamo
        self.fechaEntrega = fechaEntrega
        self.estado = "Confirmada"

        if self.fechaPrestamo > self.fechaEntrega:
            raise ValueError("La fecha de entrega no puede ser anterior a la fecha de préstamo")

    def finalizar_prestamo(self):
        self.estado = "Finalizado"
        return f"Préstamo del libro '{self.libro.titulo}' ha sido finalizado"

    def __str__(self):
        return (f"Reserva ID: {self.id_reserva} | Libro: {self.libro.titulo} | Cliente: {self.cliente.nombre} | "
                f"Fecha Préstamo: {self.fechaPrestamo} | Fecha Entrega: {self.fechaEntrega} | Estado: {self.estado}")