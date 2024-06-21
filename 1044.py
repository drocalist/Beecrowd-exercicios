A, B = map(int, input().split())
if (A < B):
    A, B = B, A
if A % B == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")