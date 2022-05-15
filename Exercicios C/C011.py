# Faça um programa que leia um número inteiro e positivo X.
# Após isso, leia sucessivos números inteiros positivos, até que um número negativo seja lido.
# Ao fim, escreva o número de vezes que o número X foi lido do usuário.

# ENTRADA:
x = int(input())

# PROCESSAMENTO:
valor_inicial = x
contador = 0
while x >= 0:
    x = int(input())
    if valor_inicial == x:
        contador += 1

# SAÍDA:
print(contador)