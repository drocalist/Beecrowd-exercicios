KM = int(input()) #distancia percorrida em km
COMBUSTIVEL = float(input()) #total de combustivel gasto


CONSUMOMEDIO = KM / COMBUSTIVEL #consumo seria a distancia dividida pelo combustivel gasto

print("{:.3f} km/l".format(CONSUMOMEDIO)) #pediu com 3 casas decimais, formatar o espaço {}
