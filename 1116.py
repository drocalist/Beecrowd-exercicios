n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        divisao = x / y
        print("%.1f"%divisao)