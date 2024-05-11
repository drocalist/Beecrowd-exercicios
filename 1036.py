import math
A, B, C = map(float, input().split()) #pontos flutuantes o a,b,c

delta = (B ** 2) - (4 * A * C) #delta
if delta < 0 or A == 0: #se o delta for menor que ou o A for igual a, não seria possivel calcular
        print("Impossivel calcular")
else:
        raiz = math.sqrt(delta) #botar o delta em uma raiz
        xlinha1 = (-B + raiz) / (2 * A) # x', como valor real da equação de segundo grau
        xlinha2 = (-B - raiz) / (2 * A) # x'', como valor real da equação de segundo grau

        print("R1 = {:.5f}".format(xlinha1)) #x'
        print("R2 = {:.5f}".format(xlinha2)) #x''