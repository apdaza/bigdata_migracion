import figuras as fg

print("primer punto")
punto_uno = fg.capturar_punto()
print("segundo punto")
punto_dos = fg.capturar_punto()

print("la distancia entre los puntos es: ",
      fg.calcular_distancia(punto_uno, punto_dos))

area_rectangulo = fg.area_rectangulo(punto_uno, punto_dos)
print("el area del rectangulo es: ", area_rectangulo)
