import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute("SELECT email, contraseña FROM usuarios")
datos = cursor.fetchall()

for email, contrasena in datos:
    print(f"Email: {email} | Contraseña: {contrasena}")

conn.close()