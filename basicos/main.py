from random import shuffle

valores = ['A', 'J', 'Q', 'K'] + [str(x) for x in range(2, 11)]
pintas = ['Diamantes', 'Corazones', 'Picas', 'Treboles']

baraja = [(v, p) for v in valores for p in pintas]

shuffle(baraja)

ganadores = ['Diamantes', 'Corazones']

jugador_1 = baraja.pop()
jugador_2 = baraja.pop()

print(jugador_1, jugador_2)

ganador_1 = ganador_2 = False

if jugador_1[1] in ganadores:
  ganador_1 = True

if jugador_2[1] in ganadores:
  ganador_2 = True

if ganador_1 == ganador_2:
  print("empate")
elif ganador_1:
  print("gana", jugador_1)
else:
  print("gana", jugador_2)


