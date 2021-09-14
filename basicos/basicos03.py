nombre = input("ingrese su nombre: ")
print("hola " + nombre * 3)

for c in nombre:
  print(c)

if len(nombre) > 5:
  print(nombre[0])
else:
  print(nombre[-1])