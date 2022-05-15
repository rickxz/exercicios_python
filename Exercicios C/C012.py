# Faça um programa que leia um número inteiro positivo N.
# Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior deles.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 1
while i <= n:
    n1 = int(input())
    if i == 1:
        maior = n1
    elif n1 > maior:
        maior = n1
    i += 1

# SAÍDA:
print(maior)