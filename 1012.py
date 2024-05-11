A, B ,C = map(float,input().split()) # 3 números flutuantes(decimais)

pi = 3.14159 #valor do pi

#formula das áreas pedidas
AreaTriangulo = (A * C)/2
AreaCirculo = (pi * C**2)
AreaTrapezio = (A + B)/2 * C
AreaQuadrado = (B * B)
AreaRetangulo = (A * B)



#print das áreas com 3 casas decimais
print("TRIANGULO: {:.3f}".format(AreaTriangulo))
print("CIRCULO: {:.3f}".format(AreaCirculo))
print("TRAPEZIO: {:.3f}".format(AreaTrapezio))
print("QUADRADO: {:.3f}".format(AreaQuadrado))
print("RETANGULO: {:.3f}".format(AreaRetangulo))