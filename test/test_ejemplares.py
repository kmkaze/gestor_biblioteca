import pytest
from src.Biblioteca import Biblioteca
from src.Libro import Libro
from src.Ejemplares import ejemplares

@pytest.fixture
def biblioteca():
    return Biblioteca()

@pytest.fixture
def ejemplar():
    return ejemplares(id=1, nombre="Biblioteca Central")

@pytest.fixture
def libro():
    return Libro(titulo="Lord of the rings", autor="J. R. R. Tolkien", isbn=1526849563125, editorial="Planeta", año=2022)

def test_agregar_libro(ejemplar, biblioteca, libro):
    resultado = ejemplar.agregar_libro(biblioteca, libro)
    assert resultado == "Libro Lord of the rings añadido"
    assert libro in biblioteca.libros

def test_eliminar_libro(ejemplar, biblioteca, libro):
    ejemplar.agregar_libro(biblioteca, libro) 
    resultado = ejemplar.eliminar_libro(biblioteca, libro)
    assert resultado == "Libro Lord of the rings eliminado del sistema"
    assert libro not in biblioteca.libros
