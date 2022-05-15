# Faça um programa que leia um número inteiro E de eleitores de um município, 
# um número inteiro B que representa o número de votos brancos, um número N 
# de votos nulos e um número V de votos válidos. 
# O programa deve calcular e escrever o percentual que cada um 
# representa em relação ao total de eleitores, 
# além da porcentagem de ausentes.

# ENTRADA:
eleitores = int(input())
brancos = int(input())
nulos = int(input())
validos = int(input())

# PROCESSAMENTO:
porcentagem_brancos = (brancos/eleitores) * 100
porcentagem_nulos = (nulos/eleitores) * 100
porcentagem_validos = (validos/eleitores) * 100
porcentagem_ausentes = (eleitores - (brancos + nulos + validos))/eleitores * 100

# SAÍDA:
print(f'Nulos: {porcentagem_nulos:.2f}%')
print(f'Brancos: {porcentagem_brancos:.2f}%')
print(f'Validos: {porcentagem_validos:.2f}%')
print(f'Ausentes: {porcentagem_ausentes:.2f}%')