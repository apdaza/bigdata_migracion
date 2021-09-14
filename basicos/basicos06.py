from math import sqrt

punto1 = input("ingrese las coordenadas separadas por coma: ")
punto1 = [int(x) for x in punto1.split(",")]

punto2 = input("ingrese las coordenadas separadas por coma: ")
punto2 = [int(x) for x in punto2.split(",")]

distancia_x = punto1[0] - punto2[0]
distancia_y = punto1[1] - punto2[1]

distancia = sqrt(distancia_x**2 + distancia_y**2)

print(distancia)