# Faça um programa que leia um valor inteiro N. 
# Após isso, leia N valores inteiros colocando-os em uma lista. 
# Em seguida, leia dois valores I e J que correspondem duas posições na lista. 
# Ao final, o programa deve escrever a soma dos elementos entre I e J, incluindo os elementos de I e J. 
# Se I ou J forem posições inválidas na lista, imprimir a mensagem INVALIDO.

# ENTRADA:
from re import I


n = int(input())
numeros = input().split()
i, j = input().split()
i, j = int(i), int(j)
# PROCESSAMENTO:
if i > len(numeros) - 1 or j > len(numeros) - 1 or i < 0 or j < 0:
    print('INVALIDO')
else:
    auxiliar = 0
    if i >= j:
        auxiliar = i
        i = j
        j = auxiliar
    soma = 0
    while i <= j:
        soma += int(numeros[i])
        i += 1
    # SAÍDA:
    print(soma)