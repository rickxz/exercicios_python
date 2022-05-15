# Faça um algoritmo que leia 2 valores inteiros A e B. Coloque-os em ordem crescente (ou seja, ao final A deve armazenar o menor valor e B o maior valor).
# Utilize o modelo abaixo apresentado no final do exercício, modificando apenas o processamento

# ENTRADA:
a = int(input())
b = int(input())

# PROCESSAMENTO:
if (a > b):
    auxiliar = b
    b = a
    a = auxiliar

# SAÍDA:
print(a)
print(b)