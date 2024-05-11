def produto(A, B): #função de produto contendo A e B
    return A * B #retornar produto entre A e B

A, B = map(int, input().split()) #integers de A e B

PROD = produto(A, B) #produto entre A e B

print(PROD)