# Faça um programa que leia um número inteiro positivo N.
# Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior, menor e a soma dos números lidos.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 1
soma = 0
while i <= n:
    n1 = int(input())
    if i == 1:
        maior = n1
        menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    soma += n1
    i += 1

# SÁIDA:
print(maior)
print(menor)
print(soma)