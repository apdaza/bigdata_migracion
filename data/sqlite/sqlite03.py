import sqlite3
try:
    bd = sqlite3.connect("test.db")
    print("Base de datos abierta")
    cursor = bd.cursor()
except sqlite3.OperationalError as error:
    print("Error al abrir", error)
finally:
    bd.close()
