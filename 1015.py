import math #incluir math da library
x1, y1 = map(float,input().split()) #ponto cartesiano 1
x2, y2 = map(float,input().split()) #ponto cartesiano 2


distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #fórmula da distancia sendo math.sqrt = raiz, logo aplicamos a raiz na fórmula concebida no exercício



print("{:.4f}".format(distancia)) #pediu a distancia com 4 casas decimais, usar o .format para incluir no espaço em {}



#outra forma

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = ((x2 - x1)**2 + (y2 - y1)**2) **(1/2)

print("{:.4f}".format(distancia))

