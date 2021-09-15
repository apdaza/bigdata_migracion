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
    condicion = {'ciudad':'Chía', 'apellido':'Daza'}
    resultado = coleccion.find_one(condicion)
    if resultado is None:
        print("No hay datos")
    else:
        for k in resultado:
            print(k + ": \t\t" + str(resultado[k]))
    
except Exception as error:
    print("Error consultando datos", error)
