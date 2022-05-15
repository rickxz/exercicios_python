# Faça um programa que leia um número inteiro N e imprima a soma de todos os fatoriais entre 0 e N (inclusive N).
# Não utilize bibliotecas matemáticas.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 0
soma = 0
while i <= n:
    if i == 0:
        soma = 1
    else: # necessário senão ele o valor da soma ficaria 1 a mais por conta do fatorial quando i == 0
        j = i
        fatorial = 1
        while j >= 1:
            fatorial *= j
            j -= 1
        soma += fatorial
    i += 1

# SAÍDA:
print(soma)