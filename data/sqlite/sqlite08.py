import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    busqueda = input("Ingrese palabra clave: ")
    sentencia = "SELECT * FROM libros WHERE titulo LIKE ?;"
    
    cursor.execute(sentencia, ["%{}%".format(busqueda)])
    
    libros = cursor.fetchall()
    print("{:^20} - {:^20} - {:^10} - {:^50}".format("autor", "género", "precio", "título"))
    for autor, genero, precio, titulo in libros:
        print("{:^20} - {:^20} - {:^10} - {:^50}".format(autor, genero, precio, titulo))
except sqlite3.OperationalError as error:
    print("Error al cponsultar", error)
finally:
    bd.close()
