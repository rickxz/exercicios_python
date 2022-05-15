# Faça um programa que leia o valor dos catetos de um triângulo retângulo e calcule a hipotenusa, de acordo com o Teorema de Pitágoras. 
# Pesquise como extrar a raiz quadrada de um número.

# ENTRADA:
cateto1 = float(input())
cateto2 = float(input())

# PROCESSAMENTO:
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5 # Extrair a raiz quadrada de um número nada mais é do que elevá-lo a 1/2.

# SAÍDA:
print(f'{hipotenusa:.2f}')