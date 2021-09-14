import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    autor = input("Autor: ")
    genero = input("Género: ")
    precio = float(input("Precio: "))
    titulo = input("Título: ")
    sentencia = """
                INSERT INTO libros(autor, genero, precio, titulo)
                VALUES (?, ?, ?, ?)
                """
    cursor.execute(sentencia, [autor, genero, precio, titulo])
    bd.commit()
    print("libro agregado correctamente")
except sqlite3.OperationalError as error:
    print("Error al insertar libro", error)
finally:
    bd.close()
