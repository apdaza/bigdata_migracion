from time import sleep

class UnidadDeTiempo:
    def __init__(self):
        self.valor = 0
        self.tope = 59

    def avanzar(self):
        if self.valor < self.tope:
            self.valor = self.valor+1
        else:
            self.valor = 0

    def resetear(self):
        self.valor = 0

    def getValor(self):
        return self.valor

class Hora(UnidadDeTiempo):
    def __init__(self):
        self.valor=0
        self.tope=23
        
class Minuto(UnidadDeTiempo):
    def __init__(self):
        self.valor=0
        self.tope=59

class Segundo(UnidadDeTiempo):
    def __init__(self):
        self.valor=0
        self.tope=59
        
class Cronometro:
    def __init__(self):
        self.h = Hora()
        self.m = Minuto()
        self.s = Segundo()

    def avanzar(self):
        self.s.avanzar()
        if(self.s.getValor()==0):
            self.m.avanzar()
            if self.m.getValor() == 0:
                self.h.avanzar()

    def getTiempo(self):
        return "{:02d}:{:02d}:{:02d}".format(self.h.getValor(), self.m.getValor(), self.s.getValor())

if __name__ == '__main__':
    c = Cronometro()
    while c.getTiempo() != "00:01:10":
        c.avanzar()
        print(c.getTiempo())
        sleep(1)

    
