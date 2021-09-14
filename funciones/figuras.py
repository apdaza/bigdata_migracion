from math import sqrt, pi

def capturar_punto():
    x = int(input("ingrese el valor de x: "))
    y = int(input("ingrese el valor de y: "))
    return x, y

def calcular_distancia(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def area_rectangulo(p1, p2):
    pt = p1[0], p2[1]
    lado1 = calcular_distancia(p1, pt)
    lado2 = calcular_distancia(p2, pt)
    area = lado1 * lado2
    return area
