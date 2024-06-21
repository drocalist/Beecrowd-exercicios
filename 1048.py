n = float(input())

for i in range(1):
    if 0 <= n <= 400:
        print("Novo salario: {:.2f}".format(n * 115/100))
        print("Reajuste ganho: {:.2f}".format(n * 15/100))
        print("Em percentual: 15 %")
    elif 400 < n <= 800:
        print("Novo salario: {:.2f}".format(n * 112 / 100))
        print("Reajuste ganho: {:.2f}".format(n * 12 / 100))
        print("Em percentual: 12 %")
    elif 800 < n <= 1200:
        print("Novo salario: {:.2f}".format(n * 110 / 100))
        print("Reajuste ganho: {:.2f}".format(n * 10 / 100))
        print("Em percentual: 10 %")
    elif 1200 < n <= 2000:
        print("Novo salario: {:.2f}".format(n * 107 / 100))
        print("Reajuste ganho: {:.2f}".format(n * 7 / 100))
        print("Em percentual: 7 %")
    else:
        print("Novo salario: {:.2f}".format(n * 104 / 100))
        print("Reajuste ganho: {:.2f}".format(n * 4 / 100))
        print("Em percentual: 4 %")