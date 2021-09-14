import sqlite3
bd = sqlite3.connect("test.db")
print("Base de datos abierta")
bd.close()
