import sqlite3
try:
    bd = sqlite3.connect("test.db")
    cursor = bd.cursor()
    libros = [
            """
                INSERT INTO libros (autor, genero, precio, titulo)
                VALUES
                ('Stephen King', 'Terror', 200, 'Resplandor'),
                ('Alejandro Daza', 'Telemedicina', 20, 'Petmud'),
                ('Alfred Bester', 'Ciencia ficción', 150, 'Las estrellas, mi destino');
            """
        ]
    for libro in libros:
        cursor.execute(libro)
    bd.commit()
    print("libros agregados")
except sqlite3.OperationalError as error:
    print("Error al insertar libro", error)
finally:
    bd.close()
