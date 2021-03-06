# A avenida principal da cidade de Algoritmopolis possui limite de velocidade de L km/h. 
# Se o motorista ultrapassar essa velocidade, é aplicado uma multa de R$ M, 
# mais R$ A por cada km acima do limite. Faça um programa que leia o limite L, 
# o valor da multa M, o valor adicional A e a velocidade V captada pelo radar 
# e informe o valor total da multa. Considere L e V sempre como números inteiros. 
# Apresente a resposta com duas casas decimais.

# ENTRADA:
limite = int(input())
multa = float(input())
adicional = float(input())
velocidade = int(input())

# PROCESSAMENTO:
if velocidade > limite:
    multa = multa + adicional * (velocidade - limite)
else:
    multa = 0

# SAÍDA:
print(f'{multa:.2f}')