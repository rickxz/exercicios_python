# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros, 
# inserindo-os em uma lista de tamanho N. 
# Em seguida, seu programa deve imprimir o maior valor informado e a posição dele na lista. 
# Se o maior valor foi informado mais de uma vez, imprimir a posição do primeiro.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
numeros = input().split()
i = maior = indice_maior = 0
while i < len(numeros):
    if i == 0:
        maior = int(numeros[0])
        indice_maior = 0
    elif int(numeros[i]) > maior:
        maior = int(numeros[i])
        indice_maior = i
    i += 1

# SAÍDA:
print(maior)
print(indice_maior)