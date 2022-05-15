# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
# Em seguida leia um número inteiro X. 
# Ao fim escreva a primeira posição na lista em que o valor X foi encontrado. 
# Se X não estiver na lista, escrever -1.

# ENTRADA:
from operator import truediv


n = int(input())
numeros = input().split()
x = int(input())

# PROCESSAMENTO:
i = indice = 0
achou = False
while i < len(numeros):
    if int(numeros[i]) == x and achou == False:
        achou = True
        indice = i
    i += 1

# SAÍDA:
if achou:
    print(indice)
else:
    print(-1)