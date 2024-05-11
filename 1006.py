def media(A, B, C): #função media contendo 1 variável com 3 parâmetros
    return (A * 2 + B * 3 + C *5)/10 #calculo da média das notas

A, B, C = map(float, input().split()) #float dos 3 parâmetros

MEDIA = media(A, B, C) #retornar o valor da média entre os 3 parâmetros

print(f"{MEDIA:.1f}") #1 casa decimal