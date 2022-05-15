# Faça um programa que leia dois números inteiros positivos X e Y e imprima todos os números de X até Y. Se X for maior que Y, imprima INVALIDO.

# ENTRADA:
x = int(input())
y = int(input())

# PROCESSAMENTO:
if x > y:
    print('INVALIDO')
else:
    while x <= y:
        print(x)
        x += 1