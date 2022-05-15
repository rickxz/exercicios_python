# Faça um programa que leia um número inteiro N e imprima a soma de todos os números primos entre 1 e N (inclusive N).

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 1
soma = 0
while i <= n:
    j = 1
    numero_divisores = 0
    while j <= i:
        if i % j == 0:
            numero_divisores += 1
        j += 1
    if numero_divisores == 2:
        soma += i
    i += 1

# SAÍDA:
print(soma)