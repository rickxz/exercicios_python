# Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X até Y, seguidos nos números de Y até X.
# Se X for maior que Y, imprima INVALIDO.

# ENTRADA:
x = int(input())
y = int(input())

# PROCESSAMENTO
if x > y:
    print('INVALIDO')
else:
    valorInicial = x
    while x <= y:
        print(x)
        x += 1
    x = valorInicial
    while y >= x:
        print(y)
        y -= 1