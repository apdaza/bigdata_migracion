from random import randint, choice

partitura = ["Do", "Re", "Mi"]

class Instrumento:
    def afinar(self):
        pass

    def tocar(self, nota = None):
        pass

class Guitarra(Instrumento):
    def afinar(self):
        print("afinando guitarra")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando guitarra")
        else:
            print("tocando guitarra en " + nota)

class Bajo(Instrumento):
    def afinar(self):
        print("afinando bajo")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando bajo")
        else:
            print("tocando bajo en " + nota)

class Flauta(Instrumento):
    def afinar(self):
        print("afinando flauta")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando flauta")
        else:
            print("tocando flauta en " + nota)

class Banda:

    def __init__(self):
        self.instrumentos = []

    def afinar(self):
        for i in self.instrumentos:
            i. afinar()

    def tocar(self):
        for i in self.instrumentos:
            i.tocar()

    def tocar_partitura(self, partitura):
        for i in self.instrumentos:
            tipo = str(type(i)).split(".")[1][:-2]
            for n in partitura:
                if tipo == "Flauta":
                    i.tocar(partitura[0])
                    break
                else:
                    i.tocar(n)

    def crear_banda(self):
        disponibles = [Guitarra(), Bajo(), Flauta()]
        cantidad = randint(3, 10)
        for i in range(cantidad):
            self.instrumentos.append(choice(disponibles))
        
            
if __name__ == '__main__':
    banda = Banda()
    banda.crear_banda()
    banda.afinar()
    banda.tocar_partitura(partitura)

