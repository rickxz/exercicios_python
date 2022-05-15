# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
# Em seguida, seu programa deve imprimir os N valores na ordem que foram lidos.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
numeros = input().split()

# SAÍDA: 
i = 0
while i < len(numeros):
    print(numeros[i], end = ' ')
    i += 1
