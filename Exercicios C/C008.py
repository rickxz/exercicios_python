# O fatorial de um número inteiro positivo N, denotado por N!, é definido como o produto dos inteiros positivos menores ou iguais a N.
# Por exemplo 4! = 4 × 3 × 2 × 1 = 24.
# Faça um programa que leia um número inteiro N e imprima o seu fatorial. Não utilize bibliotecas matemáticas.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
if n == 0:
    print(1)
else:
    i = n - 1
    while i > 1:
        n *= i
        i -= 1

    # SAÍDA:
    print(n)