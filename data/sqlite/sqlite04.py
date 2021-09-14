import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    tablas = [
            """
                CREATE TABLE IF NOT EXISTS libros(
                    autor TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    precio REAL NOT NULL,
                    titulo TEXT NOT NULL
                );
            """
        ]
    for tabla in tablas:
        cursor.execute(tabla)
    print("tablas creadas")
except sqlite3.OperationalError as error:
    print("Error al crear tabla", error)
finally:
    bd.close()
