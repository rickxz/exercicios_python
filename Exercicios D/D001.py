# Faça um programa que leia dados de temperatura durante uma semana (7 leituras), armazenando em uma lista. 
# Após isso, seu programa deve imprimir quantos dias dessa semana a temperatura esteve acima da média.

# ENTRADA:
temperaturas = input().split()

# PROCESSAMENTO:
media = 0
i = 0
while i < len(temperaturas):
    media += int(temperaturas[i])
    i += 1
    

media = media / len(temperaturas)

j = 0
contador = 0
while j < len(temperaturas):
    if int(temperaturas[j]) > media:
        contador += 1
    j += 1

# SAÍDA:
print(contador)