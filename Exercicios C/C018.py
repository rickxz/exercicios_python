# Faça um programa que leia dois números inteiros positivos A e B e faça o cálculo de multiplicação de A e B usando apenas a operação de soma.
# Imprima o resultado ao final.

# ENTRADA:
a = int(input())
b = int(input())

# PROCESSAMENTO:
i = 1
produto = 0
while i <= a:
    produto += b
    i += 1

# processo inverso:
# while i <= b:
#     produto += a
#     i += 1

# SAÍDA:
print(produto)