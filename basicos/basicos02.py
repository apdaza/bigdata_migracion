nombres = ["juan", "alejandro", "maria"]
print(type(nombres), type(nombres[0]))
print(nombres[0])

apellidos = ("diaz", "daza", "medina")
print(type(apellidos), type(apellidos[0]))
print(apellidos[0])

nombres[1] = "mario"
apellidos = (apellidos[0], apellidos[1], "salgado")

nombres.append("jose")

print(nombres)
print(apellidos)

x = 1, 2, 4
print(x, type(x))

y, w = 2, 4
print(y)
print(w)