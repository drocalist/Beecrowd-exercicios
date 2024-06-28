n = int(input())
contador = 0
for i in range(n):
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)

    media = (x * 2 + y * 3 + z * 5) / 10

    print("%.1f"%media)
    contador += 1