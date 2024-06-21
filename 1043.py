A, B, C = map(float, input().split())

Perimetro = A + B + C
TRAPEZIO = (A + B)/2 * C

if A + B > C and A + C > B and B + C > A: #você pode usar a propriedade de um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro lado
    print("Perimetro = {:.1f}".format(Perimetro))
else:
    print("Area = {:.1f}".format(TRAPEZIO))



