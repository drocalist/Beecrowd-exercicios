dias = int(input()) #Inteiro de dias, sendo o valor que será variável

ano = dias // 365 #quantos dias tem em um ano, 365, entao divide para achar 1 ano
dias = dias % 365 #resto da divisão

meses = dias // 30 #quantos dias tem em um mes,30, então divide para achar 1 mes
dias = dias % 30 #resto da divisão
#saida com ano, mes e dias, em sequência
print("{} ano(s)".format(ano))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))