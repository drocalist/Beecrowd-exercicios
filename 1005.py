def media(A, B): #definindo função media
    return (A * 3.5 + B * 7.5) / 11 #retornar a media, que seria a função

A, B = map(float, input().split()) #A e B como float

MEDIA = media(A, B) #valor da função, média da nota A com Nota B

print(f"{MEDIA:.5f}")