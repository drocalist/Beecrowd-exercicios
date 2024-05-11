r, c = map(int, input().split(".")) #split funcionou para tirar a segunda variável do caminho
c = c + r * 100 #100 centavos = 1 real

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(c // 10000))
c = c % 10000
print("{} nota(s) de R$ 50.00".format(c // 5000))
c = c % 5000
print("{} nota(s) de R$ 20.00".format(c // 2000))
c = c % 2000
print("{} nota(s) de R$ 10.00".format(c // 1000))
c = c % 1000
print("{} nota(s) de R$ 5.00".format(c // 500))
c = c % 500
print("{} notas de R$ 2.00".format(c // 200))
c = c % 200

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(c // 100))
c = c % 100
print("{} moeda(s) de R$ 0.50".format(c // 50))
c = c % 50
print("{} moeda(s) de R$ 0.25".format(c // 25))
c = c % 25
print("{} moeda(s) de R$ 0.10".format(c // 10))
c = c % 10
print("{} moeda(s) de R$ 0.05".format(c // 5))
c = c % 5
print("{} moeda(s) de R$ 0.01".format(c // 1))
c = c % 1