import pytest
from src.Biblioteca import Biblioteca
from src.Usuario import Usuario
from src.Libro import Libro

@pytest.fixture
def biblioteca():
    return Biblioteca()

@pytest.fixture
def usuario():
    return Usuario(1, "Camilo", "Duarte", "Colombia@gmail.com", "test1234")

@pytest.fixture
def libro():
    return Libro(titulo="Lord of the rings", autor="J. R. R. Tolkien", isbn=1526849563125, editorial="Planeta", año=2022)


def test_registrar_usuario(biblioteca, usuario):
    resultado = biblioteca.registrar_usuario(usuario)
    assert resultado == "Usuario registrado"
    assert usuario in biblioteca.usuarios

def test_eliminar_usuario(biblioteca, usuario):
    biblioteca.registrar_usuario(usuario)  
    resultado = biblioteca.eliminar_usuario(usuario)
    assert resultado == "Usuario eliminado"
    assert usuario not in biblioteca.usuarios

def test_ver_libros(biblioteca, libro):
    biblioteca.libros.append(libro) 
    resultado = biblioteca.ver_libros() 
    assert resultado == ["Titulo: Lord of the rings Autor: J. R. R. Tolkien Año: 2022"]  


def test_listar_usuario(biblioteca, usuario):
    biblioteca.registrar_usuario(usuario) 
    resultado = biblioteca.listar_usuario()

    assert resultado == ["Camilo, Colombia@gmail.com"]