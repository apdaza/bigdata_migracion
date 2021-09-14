diccionario = {'123': {'nombre' : 'juan', 'apellido' : 'diaz', 'edad' : 35},
              '345':  {'nombre' : 'maria', 'apellido' : 'diaz', 'edad' : 24}}

print(diccionario['345']['edad'])

for k, v in diccionario.items():
  print('llave = ', k, "valor = ", v)

matriz = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
for lista in matriz:
  for valor in lista:
    print(valor, end="\t")
  print()