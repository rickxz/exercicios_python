# Faça um programa que leia uma string S, composta apenas por uma palavra. 
# Seu programa deve imprimir os caracteres de S na ordem que aparecem em S, separados por espaço.

# ENTRADA:
s = str(input())

# PROCESSAMENTO:
for letra in s:
    print(letra, end=' ')
