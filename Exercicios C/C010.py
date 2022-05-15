# Faça um programa que leia dois números inteiros e imprima o máximo divisor comum (MDC) entre eles.
# Dica: pesquise sobre o algoritmo de euclides.

# ENTRADA:
n1 = int(input())
n2 = int(input())

# PROCESSAMENTO:
if n2 != 0:
    resto = n1%n2
    if resto == 0:
        mdc = n1//n2
    while resto != 0:
        mdc = resto
        n1 = n2
        n2 = resto
        resto = n1 % n2
        if resto != 0:
            mdc = resto

# SAÍDA:
print(mdc)