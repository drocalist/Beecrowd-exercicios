A, B, C = map(float, input())

if A >= B + C:
    print("NÃO FORMA TRIANGULO")
elif A ** 2 == B ** 2 + C ** 2:
    print("TRIANGULO RETANGULO")
elif A ** 2 > B ** 2 + C ** 2:
    print("TRIANGULO OBTUSANGULO")
elif A ** 2 < B ** 2 + C ** 2:
    print("TRIANGULO ACUTANGULO")
elif A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B != C:
    print("TRIANGULO ISOSCELES")
else:
    print("NADA")


