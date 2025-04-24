class Reservacion:
    def __init__(self, id_reserva, libro, cliente, fechaPrestamo, fechaEntrega):
        self.id_reserva = id_reserva
        self.libro = libro 
        self.cliente = cliente 
        self.fechaPrestamo = fechaPrestamo
        self.fechaEntrega = fechaEntrega
        self.estado = "Confirmada"
    
    def finalizar_prestamo(self):
        return f"Prestamo finalizado"