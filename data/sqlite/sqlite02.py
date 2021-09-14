import sqlite3
try:
    bd = sqlite3.connect("nombre_bd *//incorecto")
    print("Base de datos abierta")
    bd.close()
except sqlite3.OperationalError as error:
    print("Error al abrir", error)

