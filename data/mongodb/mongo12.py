import pymongo
from bson import ObjectId

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

try:
    coleccion = cliente[DATABASE][COLLECTION]
    condicion = {'ciudad': {'$regex': '^B'}}
    coleccion.delete_one(condicion)
    
    resultado = coleccion.find({})
    if resultado is None:
        print("No hay datos")
    else:
        for e in resultado:
            for k in e:
                print(k + ": \t\t" + str(e[k]))
            print("")
    
except Exception as error:
    print("Error consultando datos", error)
