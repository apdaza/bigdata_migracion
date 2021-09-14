import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    busqueda = input("Ingrese id libro: ")
    
    sentencia = "DELETE FROM libros WHERE rowid = ?;"
                
    cursor.execute(sentencia, [busqueda])
    bd.commit()
    print("libro borrado")


    sentencia = "SELECT * FROM libros;"
    
    cursor.execute(sentencia)
    
    libros = cursor.fetchall()
    print("{:^15} - {:^15} - {:^5} - {:^30}".format("autor", "género", "precio", "título"))
    for autor, genero, precio, titulo in libros:
        print("{:^15} - {:^15} - {:^5} - {:^30}".format(autor, genero, precio, titulo))
except sqlite3.OperationalError as error:
    print("Error al consultar", error)
finally:
    bd.close()
