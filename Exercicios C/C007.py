# Faça um programa que leia dois números inteiros não negativos A e B, onde A é a base e B é o expoente de uma potência.
# Após isso, calcule e imprima o valor de A elevado a B. Não utilize bibliotecas matemáticas.
# No caso de python, não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.

# ENTRADA:
a = int(input())
b = int(input())

# a^b = a * a * a... (b vezes)

# PROCESSAMENTO:
i = 1
base = a
if b == 0:
    print(1)
else:
    while i < b:
        a *= base
        i += 1

    # SAÍDA:
    print(a)