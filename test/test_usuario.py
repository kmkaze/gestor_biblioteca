import pytest
from src.Usuario import Usuario
from src.Libro import Libro

@pytest.fixture
def usuario():
    return Usuario(1, "Camilo", "Duarte", "Colombia@gmail.com", "test1234")

@pytest.fixture
def libro():
    return Libro(titulo="Lord of the rings", autor="J. R. R. Tolkien", isbn=1526849563125, editorial="Planeta", año=2022)

def test_creacion_usuario():
    user1 = Usuario(2,"Fredy","Urrego","urrego@gmail.com",12345)
    
    assert user1.id_cliente == 2
    assert user1.nombre == "Fredy"
    assert user1.apellido == "Urrego"
    assert user1.email == "urrego@gmail.com"
    assert user1.contraseña == 12345

def test_inicio_sesion_correcto(usuario):
    assert usuario.inicio_sesion("Colombia@gmail.com", "test1234") == True

def test_inicio_sesion_incorrecto(usuario):
    assert usuario.inicio_sesion("Colombia@gmail.com", "fake ") == False

def test_nueva_reserva(usuario, libro):
    resultado = usuario.nueva_reserva(libro)
    assert resultado == f"Libro {libro.titulo} prestado"
    assert libro in usuario.reservas
    assert libro.disponible is False

def test_devolver_libro(usuario, libro):
    usuario.reservas.append(libro)
    resultado = usuario.devolver_libro(libro)
    
    assert resultado == f"Libro {libro.titulo} devuelto"

    
def test_ver_reservas(usuario, libro):
    usuario.reservas.append(libro)
    resultado = usuario.ver_reservas()
    
    assert resultado == ["Lord of the rings"]


