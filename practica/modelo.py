import pymongo
from bson import ObjectId

HOST = "127.0.0.1"
PORT = "27017"
DATABASE = 'capacitacion'
COLLECTION = 'usuarios'
URI_CONEXION = "mongodb://" + HOST + ":" + PORT + "/"

def consultar():
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        cliente.server_info()
        print("Conexión OK")
        cliente.close()
    except pymongo.errors.ConnectionFailure as error:
        print("No se puede conectar a Mongo", error)

    try:
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {}
        resultado = coleccion.find(condicion)
        data = resultado
    except Exception as error:
        print("Error consultando datos", error)

    finally:
        return data

def insertar(data):
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        cliente.server_info()
        print("Conexión OK")
        cliente.close()
    except pymongo.errors.ConnectionFailure as error:
        print("No se puede conectar a Mongo", error)

    try:
        coleccion = cliente[DATABASE][COLLECTION]
        coleccion.insert_one(data)
        print("data insertada")
    except Exception as error:
        print("Error insertando datos", error)

def eliminar_porid(id):
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        cliente.server_info()
        print("Conexión OK")
        cliente.close()
    except pymongo.errors.ConnectionFailure as error:
        print("No se puede conectar a Mongo", error)

    try:
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        coleccion.delete_one(condicion)
        
    except Exception as error:
        print("Error consultando datos", error)
    
