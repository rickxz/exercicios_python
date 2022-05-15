# Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas. 
# Faça um programa que leia o valor total da compra e um valor de desconto 
# (de 0 a 100, representando a porcentagem de desconto). 
# O programa de escrever o valor da compra com o desconto aplicado. 
# Escreva a saída com duas casas decimais.

# ENTRADA:
valor_total = float(input())
valor_desconto = float(input())

# PROCESSAMENTO:
valor_compra = valor_total - (valor_total * valor_desconto)/100

# SAÍDA:
print(f'{valor_compra:.2f}')