#Faça um programa que leia duas notas de provas e calcule e escreva a média simples delas. 
# Escreva a saída com duas casas decimais.

# ENTRADA:
nota1 = float(input())
nota2 = float(input())

# PROCESSAMENTO:
media = (nota1 + nota2) / 2

# SAÍDA:
print('{:.2f}'.format(media))
# print(f'{media:.2f}') ---> maneira alternativa