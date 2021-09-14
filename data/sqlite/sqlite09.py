import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    busqueda = input("Ingrese id libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    precio = float(input("Precio: "))
    titulo = input("Título: ")
    sentencia = """
                UPDATE libros SET autor = ?,
                                  genero = ?,
                                  precio = ?,
                                  titulo = ?
                WHERE rowid = ?;
                """
    cursor.execute(sentencia, [autor, genero, precio, titulo, busqueda])
    bd.commit()


    sentencia = "SELECT * FROM libros;"
    
    cursor.execute(sentencia)
    
    libros = cursor.fetchall()
    print("{:^15} - {:^15} - {:^5} - {:^30}".format("autor", "género", "precio", "título"))
    for autor, genero, precio, titulo in libros:
        print("{:^15} - {:^15} - {:^5} - {:^30}".format(autor, genero, precio, titulo))
except sqlite3.OperationalError as error:
    print("Error al cponsultar", error)
finally:
    bd.close()
