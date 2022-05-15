# Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
# Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Faça um programa que leia um número inteiro positivo N e imprima 1 se ele for primo e 0 caso contrário.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 1
numero_divisores = 0 # o número de divisores de um número primo sempre será dois (1 e ele mesmo)
while i <= n:
    if n % i == 0:
        numero_divisores += 1
    i += 1

# SAÍDA:
if numero_divisores == 2:
    print(1)
else:
    print(0)