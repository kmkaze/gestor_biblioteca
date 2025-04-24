import pytest
from src.Libro import Libro

@pytest.fixture
def libro():
    return Libro(titulo="Lord of the rings", autor="J. R. R. Tolkien", isbn=1526849563125, editorial="Planeta", año=2022)

def test_crear_libro(libro):
    assert libro.titulo == "Lord of the rings"
    assert libro.autor == "J. R. R. Tolkien"
    assert libro.isbn == 1526849563125
    assert libro.editorial == "Planeta"
    assert libro.año == 2022
    
def test_mostrar_informacion(libro):
    resultado = "Titulo: Lord of the rings Autor: J. R. R. Tolkien Año: 2022"
    assert libro.mostrar_informacion() == resultado

def test_actualizar_disponibilidad(libro):

    assert libro.actualizar_disponibilidad(True) == "El libro Lord of the rings - Estado disponible"
    assert libro.disponible == True  
    
    assert libro.actualizar_disponibilidad(False) == "El libro Lord of the rings - Estado no disponible"
    assert libro.disponible == False  