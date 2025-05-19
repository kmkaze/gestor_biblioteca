from src.Biblioteca import Biblioteca
from src.Libro import Libro

libros = [
    {
        "ISBN": "978-0-45-152493-5",
        "titulo": "1984",
        "autor": "George Orwell",
        "editorial": "Signet Classics",
        "año": 1949
    },
    {
        "ISBN": "978-0-30-747472-8",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "editorial": "Editorial Sudamericana",
        "año": 1967
    },
    {
        "ISBN": "978-0-15-601219-5",
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "editorial": "Reynal & Hitchcock",
        "año": 1943
    },
    {
        "ISBN": "978-8-49-105204-3",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "editorial": "Francisco de Robles",
        "año": 1605
    },
    {
        "ISBN": "978-8-40-817217-4",
        "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "editorial": "Planeta",
        "año": 2001
    },
    {
        "ISBN": "978-9-50-987588-3",
        "titulo": "El laberinto de la soledad",
        "autor": "Octavio Paz",
        "editorial": "Ediciones Era",
        "año": 1950
    },
    {
        "ISBN": "978-8-49-759099-9",
        "titulo": "Rayuela",
        "autor": "Julio Cortázar",
        "editorial": "Lumen",
        "año": 1963
    },
    {
        "ISBN": "978-0-30-738973-2",
        "titulo": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez",
        "editorial": "Penguin",
        "año": 1985
    },
    {
        "ISBN": "978-0-38-550420-1",
        "titulo": "El código Da Vinci",
        "autor": "Dan Brown",
        "editorial": "Doubleday",
        "año": 2003
    },
    {
        "ISBN": "978-0-26-110357-3",
        "titulo": "El señor de los anillos: La comunidad del anillo",
        "autor": "J.R.R. Tolkien",
        "editorial": "Allen & Unwin",
        "año": 1954
    },
    {
        "ISBN": "978-0-06-231500-7",
        "titulo": "El alquimista",
        "autor": "Paulo Coelho",
        "editorial": "HarperOne",
        "año": 1988
    },
    {
        "ISBN": "978-0-14-143957-0",
        "titulo": "El retrato de Dorian Gray",
        "autor": "Oscar Wilde",
        "editorial": "Ward, Lock & Co.",
        "año": 1890
    },
    {
        "ISBN": "978-1-45-167331-9",
        "titulo": "Fahrenheit 451",
        "autor": "Ray Bradbury",
        "editorial": "Ballantine Books",
        "año": 1953
    },
    {
        "ISBN": "978-0-06-112008-4",
        "titulo": "Matar a un ruiseñor",
        "autor": "Harper Lee",
        "editorial": "J.B. Lippincott & Co.",
        "año": 1960
    },
    {
        "ISBN": "978-1-50-329056-3",
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "editorial": "T. Egerton",
        "año": 1813
    },
    {
        "ISBN": "978-0-31-676948-8",
        "titulo": "El guardián entre el centeno",
        "autor": "J.D. Salinger",
        "editorial": "Little, Brown and Company",
        "año": 1951
    },
    {
        "ISBN": "978-0-67-978158-5",
        "titulo": "Memorias de una geisha",
        "autor": "Arthur Golden",
        "editorial": "Alfred A. Knopf",
        "año": 1997
    },
    {
        "ISBN": "978-9-50-072370-5",
        "titulo": "La tregua",
        "autor": "Mario Benedetti",
        "editorial": "Seix Barral",
        "año": 1960
    },
    {
        "ISBN": "978-0-39-332779-9",
        "titulo": "El niño con el pijama de rayas",
        "autor": "John Boyne",
        "editorial": "David Fickling Books",
        "año": 2006
    },
    {
        "ISBN": "978-0-06-231609-7",
        "titulo": "Sapiens: De animales a dioses",
        "autor": "Yuval Noah Harari",
        "editorial": "Debate",
        "año": 2011
    }
]

def cargar_libros():
    biblioteca = Biblioteca(db_path="biblioteca.db")
    for libro_dict in libros:
        libro_obj = Libro(
            None,
            libro_dict["titulo"],
            libro_dict["autor"],
            libro_dict["ISBN"],
            libro_dict["editorial"],
            libro_dict["año"],
            True  
        )
        resultado = biblioteca.registrar_libro(libro_obj)
        print(resultado)

if __name__ == "__main__":
    cargar_libros()