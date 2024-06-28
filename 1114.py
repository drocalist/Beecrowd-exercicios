
ciclo = True
while ciclo:
    password = int(input())
    if password == 2002:
        print("Acesso Permitido")
        ciclo = False
    else:
        print("Senha Invalida")