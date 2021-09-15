import pymongo

HOST = "127.0.0.1"
PORT = "27017"
DATABASE = 'capacitacion'
COLLECTION = 'usuarios'
URI_CONEXION = "mongodb://" + HOST + ":" + PORT + "/"

try:
    cliente = pymongo.MongoClient(URI_CONEXION)
    cliente.server_info()
    print("Conexión OK")
    cliente.close()
except pymongo.errors.ConnectionFailure as error:
    print("No se puede conectar a Mongo", error)

data = [
        {'nombre': 'Juan', 'apellido': 'Perez', 'ciudad': 'Bogotá'},
        {'nombre': 'Ana', 'apellido': 'Diaz', 'ciudad': 'Cota'},
        {'nombre': 'Antonia', 'apellido': 'Mendez', 'ciudad': 'Chía'}
    ]    

try:
    coleccion = cliente[DATABASE][COLLECTION]
    coleccion.insert_many(data)
    print("data insertada")
except Exception as error:
    print("Error insertando datos", error)
