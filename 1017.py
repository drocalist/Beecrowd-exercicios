h = int(input()) #horas na viagem percorrida
v = int(input()) #velocidade média na viagem


KM = 1 #Embutir um valor para não ser nulo
L = 1 #Embutir um valor para não ser nulo
consumo_do_automovel = 12 * KM/L #consumo do automóvel

distancia = (h * v) / consumo_do_automovel # Velocidade x tempo / pelo consumo do automóvel

print("{:.3f}".format(distancia))

# Velocidade média x tempo = distancia em uma viagem

