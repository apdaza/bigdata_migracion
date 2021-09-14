from random import choice

saludos = ["hello", "hola", "chao"]

def saludo(nombre):
    return "%s %s, cómo estás?" % (choice(saludos), nombre)


if __name__ == '__main__':
    print(saludo("juan"))
