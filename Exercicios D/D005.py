# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
# Em seguida leia um número inteiro X.
# Ao fim escreva o número de vezes que o número X foi lido do usuário.

# ENTRADA:
n = int(input())
numeros = input().split()
x = int(input())

# PROCESSAMENTO:
i = contador = 0
while i < len(numeros):
    if int(numeros[i]) == x:
        contador += 1
    i += 1

# SAÍDA:
print(contador)