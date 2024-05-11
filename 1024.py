N = int(input()) #casos de teste
outputs = [] #saida

while (N > 0):
    M = input()
    word = []

    for i in range(len(M)): #itera sobre M
        word.append(M[i])

    for i in range(len(word)): #itera sobre word
        if(word[i].isalpha()): #tem que estar no alfabeto
            novo = ord(word[i]) + 3 #deslocar 3 casas
            word[i] = chr(novo)

    word.reverse()

    metade = len(word) // 2

    for i in range(metade, len(word)):
        novo = ord(word[i]) - 1 #desloca 1 casa
        word[i] = chr(novo)

    word = "".join(word)
    outputs.append(word)
    N -= 1 #decrementa 1

for i in range(len(outputs)):
    print(outputs[i])






