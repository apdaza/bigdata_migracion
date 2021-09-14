def suma(numero_1, numero_2):
    respuesta = numero_1 + numero_2
    return respuesta

def resta(numero_1, numero_2):
    respuesta = numero_1 - numero_2
    return respuesta

def producto(numero_1, numero_2):
    respuesta = numero_1 * numero_2
    return respuesta

def division(numero_1, numero_2):
    respuesta = numero_1 // numero_2
    return respuesta

if __name__ == '__main__':
    numero_uno = int(input("ingrese un número: "))
    numero_dos = int(input("ingrese un número: "))

    var = suma(numero_uno, numero_dos)
    print(var)

    var = resta(numero_uno, numero_dos)
    print(var)

    var = producto(numero_uno, numero_dos)
    print(var)

    var = division(numero_uno, numero_dos)
    print(var)
