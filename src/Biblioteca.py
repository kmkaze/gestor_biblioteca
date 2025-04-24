class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.administradores = []
        
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return f"Usuario registrado"

    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            return f"Usuario eliminado"
            
    def ver_libros(self):
            return [libro.mostrar_informacion() for libro in self.libros]

    def listar_usuario(self):
        return [f"{usuario.nombre}, {usuario.email}" for usuario in self.usuarios]
