from src.Reservacion import Reservacion
from src.Libro import Libro
import pytest

@pytest.fixture
def reserva():
    libro = Libro(titulo="Lord of the rings", autor="J. R. R. Tolkien", isbn="12345", editorial="Planeta", año=2022)
    return Reservacion(id_reserva=1, libro=libro, cliente="Freddy", fechaPrestamo="2025-05-01", fechaEntrega="2025-05-15")

def test_finalizar_prestamo(reserva):
    resultado = reserva.finalizar_prestamo()  
    assert resultado == "Prestamo finalizado" 