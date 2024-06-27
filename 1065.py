def contar_pares():
    numeros = []
    pares = 0
    tamanho = 5
    for i in range(tamanho):
        numero = int(input())
        numeros.append(numero)

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1

    print("%s valores pares"%pares)

contar_pares()
