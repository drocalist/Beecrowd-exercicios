#número que queremos dividir
n = int(input())

#notas armazenadas
notas = [100, 50, 20, 10, 5, 2, 1]

#divisão e divisão inteira do número
notas100 = n // 100
n = n % 100

notas50 = n // 50
n = n % 50

notas20 = n // 20
n = n % 20

notas10 = n // 10
n = n % 10

notas5 = n // 5
n = n % 5

notas2 = n // 2
n = n % 2

notas1 = n // 1
n = n % 1

#Notas dos numeros anteriormente armazenadas e os valores em reais
print("{} nota(s) de R$ {:.2f}".format(notas100, notas[0]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas50, notas[1]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas20, notas[2]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas10, notas[3]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas5, notas[4]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas2, notas[5]).replace(".", ","))
print("{} nota(s) de R$ {:.2f}".format(notas1, notas[6]).replace(".", ","))


#
n = int(input())

print(n)


notas100 = n // 100
n = n % 100

notas50 = n // 50
n = n % 50

notas20 = n // 20
n = n % 20

notas10 = n // 10
n = n % 10

notas5 = n // 5
n = n % 5

notas2 = n // 2
n = n % 2

notas1 = n // 1
n = n % 1

print("{} nota(s) de R$ 100,00" .format(notas100))
print("{} nota(s) de R$ 50,00" .format(notas50))
print("{} nota(s) de R$ 20,00" .format(notas20))
print("{} nota(s) de R$ 10,00" .format(notas10))
print("{} nota(s) de R$ 5,00" .format(notas5))
print("{} nota(s) de R$ 2,00" .format(notas2))
print("{} nota(s) de R$ 1,00" .format(notas1))

