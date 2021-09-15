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

try:
    coleccion = cliente[DATABASE][COLLECTION]
    condicion = {}
    resultado = coleccion.find(condicion)
    for elemento in resultado:
        for k in elemento:
            print(k + "\t : \t" + str(elemento[k]))
    
except Exception as error:
    print("Error consultando datos", error)
