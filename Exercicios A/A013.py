# Faça um programa que leia um número inteiro S que representa uma quantidade de segundos. 
# Seu programa deve imprimir quatro valores inteiros, que representem a 
# quantidade de segundos S em dias, horas, minutos e segundos. 
# Por exemplo, 188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos. 
# Dica: lembre-se dos operadores resto e divisão inteira.

# 1 dia: 86400 segundos
# 1 hora: 3600 segundos
# 1 minuto: 60 segundos

# ENTRADA:
s = int(input())

# PROCESSAMENTO:
dias = s//86400
resto = s%86400

horas = resto//3600
resto = resto % 3600 # ou resto %= 3600

minutos = resto//60
resto = resto%60 # o que sobrou são os segundos!

# SAÍDA:
print(dias, horas, minutos, resto)