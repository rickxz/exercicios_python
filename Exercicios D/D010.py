# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
# A cada valor lido, o programa deve inserir em uma lista A se o valor 
# for par e em uma lista B se o valor for ímpar. 
# Ao fim, escreva as duas listas resultantes, na primeira linha a lista A e na segunda a lista B.

# ENTRADA:
n = int(input())
numeros = input().split()

# PROCESSAMENTO:
lista_pares = []
lista_impares = []
i = 0
while i < len(numeros):
    if int(numeros[i]) % 2 == 0:
        lista_pares.append(int(numeros[i]))
    else:
        lista_impares.append(int(numeros[i]))
    i += 1

# SAÍDA:
i = 0
if len(lista_pares) == 0:
    print()
else:
    while i < len(lista_pares):
        print(int(lista_pares[i]), end = ' ')
        i += 1
print()
i = 0
if len(lista_impares) == 0:
    print()
else:
    while i < len(lista_impares):
        print(int(lista_impares[i]), end = ' ')
        i += 1