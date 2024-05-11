segundos = int(input()) #segundos como inteiro, sendo variável

horas = segundos // 3600 #quantos segundos existem em 1 hora
segundos = segundos % 3600 #resto

minutos = segundos // 60 #quantos segundos existem em 1 minuto
segundos = segundos % 60 #resto

#saida com horas, minutos, segundos
print("{}:{}:{}".format(horas, minutos, segundos))