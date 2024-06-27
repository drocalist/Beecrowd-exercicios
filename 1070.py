X = int(input())

contador = 0
impares_consecutivos = X

for i in range(12):
    if impares_consecutivos % 2 == 1:
        print(impares_consecutivos)
        contador += 1
    impares_consecutivos += 1
