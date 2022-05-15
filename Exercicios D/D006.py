# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
# Em seguida, seu programa deve imprimir os N valores na ordem inversa que foram lidos.

# ENTRADA;
n = int(input())
numeros = input().split()

# PROCESSAMENTO:
i = len(numeros) - 1
while i >= 0:
    print(int(numeros[i]), end = ' ')
    i -= 1
