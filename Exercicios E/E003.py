# Faça um programa que leia uma string S e um caractere C. 
# Ao fim escreva o número de vezes que o caractere C aparece na string S.

# ENTRADA:
s = str(input())
c = str(input())

# PROCESSAMENTO:
contador = 0
for letra in s:
    if letra == c:
        contador += 1

# SAÍDA:
print(contador)