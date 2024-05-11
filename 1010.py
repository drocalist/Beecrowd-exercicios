def produto(numero_peça1, valor_unitario_peça1, numero_peça2, valor_unitario_peça2): #função produto
    return (numero_peça1 * valor_unitario_peça1) + (numero_peça2 * valor_unitario_peça2) #numero de peças 1 com valor unitario 1, repetindo no 2 caso

codigo_peça1, numero_peça1, valor_unitario_peça1, codigopeça2, numero_peça2, valor_unitario_peça2 = input().split() #6 parametros, 4 integers e 2 floats, se referindo a peças e valor delas
codigo_peça1 = int(codigo_peça1)
numero_peça1 = int(numero_peça1)
valor_unitario_peça1 = float(valor_unitario_peça1)
codigopeça2 = int(codigopeça2)
numero_peça2 = int(numero_peça2)
valor_unitario_peça2 = float(valor_unitario_peça2)

VALOR_A_PAGAR = produto(numero_peça1, valor_unitario_peça1, numero_peça2, valor_unitario_peça2) #valor a pagar

print(VALOR_A_PAGAR)




