from flask import Flask, render_template, redirect, url_for, flash, request, session
from src.Biblioteca import Biblioteca
from src.Usuario import Usuario
from src.Libro import Libro

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  


biblioteca = Biblioteca()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        usuario = biblioteca.buscar_usuario(email)
        if usuario and usuario.inicio_sesion(email, contraseña):

            session["usuario"] = usuario.email

            if usuario.email.lower() == "admin@biblioconnect.com":
                return redirect(url_for("menu_admin"))
            else:
                return redirect(url_for("menu_usuario"))
        else:
            flash("Usuario o contraseña incorrectos")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/menu_admin")
def menu_admin():
    return render_template("menu_admin.html")

@app.route("/menu_usuario")
def menu_usuario():
    email_usuario = session.get("usuario")
    if not email_usuario:
        flash("Debes iniciar sesión", "warning")
        return redirect(url_for("login"))
    

    usuario_actual = biblioteca.buscar_usuario(email_usuario)
    
    reservas = usuario_actual.reservas  
    
    return render_template("menu_usuario.html", reservados=reservas)

@app.route("/gestionar_libros")
def gestionar_libros():
    libros = biblioteca.cargar_libros()
    return render_template("gestionar_libros.html", libros=libros)

@app.route("/agregar_libro", methods=["GET", "POST"])
def agregar_libro():
    if request.method == "POST":
        isbn = request.form.get("isbn")
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        editorial = request.form.get("editorial")
        año = request.form.get("año")
        
        # Validar que todos los campos estén completos
        if not all([isbn, titulo, autor, editorial, año]):
            flash("Todos los campos son obligatorios")
            return redirect(url_for("agregar_libro"))
        
        try:
            año_int = int(año)
        except ValueError:
            flash("El año debe ser un número")
            return redirect(url_for("agregar_libro"))
        
        # Instanciar un nuevo libro (el 'id' se asigna automáticamente si es autoincrement)
        nuevo_libro = Libro(None, titulo, autor, isbn, editorial, año_int, disponible=True)
        
        # Registrar el nuevo libro en la base de datos
        if biblioteca.registrar_libro(nuevo_libro):
            flash("Libro agregado exitosamente!")
        else:
            flash("Error al agregar el libro")
        
        # Actualizar la lista de libros y redirigir al menú de administrador
        biblioteca.libros = biblioteca.cargar_libros()
        return redirect(url_for("gestionar_libros"))
    
    # Para GET, mostrar el formulario para agregar un libro
    return render_template("agregar_libro.html")

@app.route("/eliminar_libro", methods=["GET", "POST"])
def eliminar_libro():
    if request.method == "POST":

        titulo = request.form.get("titulo")
        if not titulo:
            flash("Debe proporcionar el título del libro")
            return redirect(url_for("eliminar_libro"))
        
        if biblioteca.eliminar_libro(titulo):
            flash("Libro eliminado exitosamente!")
        else:
            flash("No se encontró el libro o hubo un error al eliminarlo.")

        biblioteca.libros = biblioteca.cargar_libros()
    return render_template("eliminar_libro.html")

@app.route("/ver_libros")
def ver_libros():
    biblioteca.libros = biblioteca.cargar_libros()
    return render_template("ver_libros.html", libros=biblioteca.libros)

@app.route("/reservar", methods=["GET", "POST"])
def reservar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        if not titulo:
            flash("Debe proporcionar el título del libro", "warning")
            return redirect(url_for("reservar"))
        
        libros_disponibles = biblioteca.cargar_libros()
        libro = next((l for l in libros_disponibles if l.titulo.lower() == titulo.lower()), None)
        if libro is None:
            flash("No se encontró el libro", "warning")
            return redirect(url_for("reservar"))
         
        usuario = biblioteca.buscar_usuario(session["usuario"])
        if not usuario:
            flash("Error al identificar el usuario", "warning")
            return redirect(url_for("login"))
        
        mensaje = usuario.reservar_libro(libro)
        flash(mensaje, "success")
        
    return render_template("reservar.html")

@app.route("/gestionar_usuarios")
def gestionar_usuarios():
    usuarios = biblioteca.cargar_usuarios()
    return render_template("gestionar_usuarios.html", usuarios=usuarios)

@app.route("/agregar_usuario", methods=["GET", "POST"])
def agregar_usuario():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        
        if not all([nombre, apellido, email, contraseña]):
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for("agregar_usuario"))
        
        nuevo_usuario = Usuario(None, nombre, apellido, email, contraseña)
        
        if biblioteca.registrar_usuario(nuevo_usuario):
            flash("Usuario agregado exitosamente!", "success")
        else:
            flash("Error al agregar el usuario", "warning")
        
    
    return render_template("agregar_usuario.html")

@app.route("/eliminar_usuario", methods=["GET", "POST"])

def eliminar_usuario():
    if request.method == "POST":

        email = request.form.get("email")
        if not email:
            flash("Debe proporcionar el email del usuario", "warning")
            return redirect(url_for("eliminar_usuario"))

        if biblioteca.eliminar_usuario(email):
            flash("Usuario eliminado exitosamente!", "success")
        else:
            flash("No se encontró el usuario o hubo un error al eliminarlo.", "warning")

    return render_template("eliminar_usuario.html")

@app.route("/devolver", methods=["GET", "POST"])
def devolver():
    if request.method == "POST":

        titulo = request.form.get("titulo")
        if not titulo:
            flash("Debe proporcionar el título del libro a devolver.", "warning")
            return redirect(url_for("devolver"))
        
        email_usuario = session.get("usuario")
        if not email_usuario:
            flash("Debes iniciar sesión para devolver un libro.", "warning")
            return redirect(url_for("login"))
        
        usuario_actual = biblioteca.buscar_usuario(email_usuario)
        if not usuario_actual:
            flash("Usuario no encontrado.", "warning")
            return redirect(url_for("login"))
        
        mensaje = usuario_actual.devolver_libro(titulo)
        
        return redirect(url_for("menu_usuario"))
    
    return render_template("devolver.html")

if __name__ == '__main__':
    app.run(debug=True)