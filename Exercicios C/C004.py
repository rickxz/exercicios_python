# Faça um programa que leia dois números inteiros N e M e imprima a soma de todos os números entre eles (inclua N e M na soma).
# Faça sua solução utilizando laço de repetição.

# ENTRADA:
n = int(input())
m = int(input())

# PROCESSAMENTO:
soma = 0
if m > n:
    while n <= m:
        soma += n
        n += 1
else:
    while m <= n:
        soma += m
        m += 1

# SAÍDA:
print(soma)