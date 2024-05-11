def soma(A, B): #definindo variável soma contendo a e b
    return A + B #retornar A somando com B

A, B = map(int, input().split()) #integers de A e B
SOMA = soma(A, B) #função de A e B, no caso a soma

print(SOMA)