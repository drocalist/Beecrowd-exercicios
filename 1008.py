def produto(HORAS, VALOR): #produto entre horas e valor
    return HORAS * VALOR #horas * valor = trabalhador do Brasil

COD, HORAS, VALOR = input().split() #3 parametros, 2 integers e 1 float
COD = int(COD)
HORAS = int(HORAS)
VALOR = float(VALOR)

QUANTIDADE_TRABALHADA = produto(HORAS, VALOR) #quanto o trabalhador ganha

#código e dinheiro ganhado no final do mes
print(COD)
print(QUANTIDADE_TRABALHADA)