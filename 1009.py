def produto(SALARIO, VENDAS): #produto
    return (SALARIO + VENDAS * 15/100) #soma entre salario e vendas junto com a comissão de 15%


VENDEDOR, SALARIO, VENDAS = input().split() #3 parâmetros com 1 input e 2 floats
VENDEDOR = input(VENDEDOR)
SALARIO = float(SALARIO)
VENDAS = float(VENDAS)

QUANTO_GANHA = produto(SALARIO, VENDAS) #quanto ele ganha

print(VENDEDOR)
print(QUANTO_GANHA)


