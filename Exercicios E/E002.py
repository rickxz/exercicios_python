# Faça um programa que leia uma string S, composta apenas por uma palavra.
# Seu programa deve imprimir os caracteres de S na ordem inversa que aparecem em S, separados por espaço.

# ENTRADA?
s = str(input())

# PROCESSAMENTO:
for i in range(len(s) - 1, -1, -1):
    print(s[i], end= ' ')
