# Faça um programa que leia um número natural N e imprima o número harmônico de ordem N. Um número harmônico H é definido por:
# H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
# Imprima o resultado com 4 casas decimais.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
harmonico = 0
i = 1
while i <= n:
    harmonico += 1/i
    i += 1

# SAÍDA:
print(f'{harmonico:.4f}')