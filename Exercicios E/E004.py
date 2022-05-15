# Faça um programa que leia uma string S e imprima 1 se ela é palíndromo e 0 caso contrário. 
# Uma string é palíndromo se quando lido da esquerda para a direita é igual ao ser lido da direita 
# para a esquerda. Exemplos: "arara", "amor e roma". 
# Observações importantes: 
# 1) Seu programa deve desconsiderar caracteres de espaço; 
# 2) Seu programa NÃO deve criar uma string auxiliar, ou seja, ele deve dizer se a string 
# é palíndromo apenas acessando/consultando seus caracteres.

# ENTRADA:
s = str(input())

# PROCESSAMENTO:
diferente = False # caso ache um caractere diferente, não é um palíndromo
for i in range(len(s)):
    indice_direita = len(s) - (i + 1)
    if s[i] != s[indice_direita] and s[i] != ' ' and s[indice_direita] != ' ': # se os caracteres diferentes e não forem espaços
        print(s[i] +  ' ' + s[indice_direita])
        diferente = True
        break

# SAÍDA:
if diferente:
    print(0)
else:
    print(1)