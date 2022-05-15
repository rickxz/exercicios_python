# Faça um programa que leia um número inteiro (assuma que esse número terá 4 digitos obrigatoriamente) 
# e inverta esse número. Por fim escreva o número invertido. 
# O seu programa deve apenas manipular números inteiros. Não é permitido usar strings, lista, etc.

# ENTRADA:

numero = int(input()) 

# PROCESSAMENTO:
unidade = numero%10
resto = numero//10

dezena = resto%10
resto //= 10 # ou resto//= 10

centena = resto%10
resto = resto//10 # o número da milhar é o que restou

invertido = unidade * 1000 + dezena * 100 + centena * 10 + resto

# SAÍDA:
print(invertido)