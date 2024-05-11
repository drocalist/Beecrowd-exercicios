def diferenca(A, B, C, D): #função diferenca
    return (A * B - C * D) #diferença entre a*b e c*d

A, B, C, D = input().split() #4 parametros com 4 integers
A = int(A)
B = int(B)
C = int(C)
D = int(D)

DIFERENCA = diferenca(A, B, C, D) #diferença

print(DIFERENCA) #print da diferença