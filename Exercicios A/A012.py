#Sabe-se que uma lata de tinta tem um custo C e é capaz de pintar uma área de M metros quadrados. 
# Faça um programa que leia a largura L, a altura A de uma parede, o valor C de uma lata de tinta 
# e o rendimento M desta lata. Após isso, imprima quantas latas de tintas são necessárias 
# e o custo total (com duas casas decimais). Assuma que não é possível comprar lata de tinta fracionada.

import math
# ENTRADA:
largura = float(input())
altura = float(input())
valor = float(input())
rendimento = float(input())

# PROCESSAMENTO:
area = largura * altura
latas_necessarias = math.ceil(area/rendimento) # Arredonda para o próximo número inteiro maior
custo_total = latas_necessarias * valor

# SAÍDA:
print(latas_necessarias)
print(f'{custo_total:.2f}')