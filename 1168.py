N = int(input()) #n vezes de teste

leds = { #dicionário armazenando a string dos numeros com cada led necessário
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}

for i in range(N): #n vezes percorrerá as linhas seguintes
    numero = input() #digitar um número como string
    total_leds = sum(leds[i] for i in numero) #somar as strings do número e converte em leds
    if total_leds > 0: #se a soma dos leds for maior que 0 então printa
        print("{} leds".format(total_leds))









