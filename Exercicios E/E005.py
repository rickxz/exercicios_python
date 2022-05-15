# Faça um programa que leia duas strings A e B, e imprima 1 se A e B são anagramas e 0, caso contrário. 
# Anagrama é a transposição de letras de palavra ou frase para formar outra palavra ou frase diferente. 
# Por exemplo: "algoritmo" e “logaritmo” são anagramas. 
# Seu programa deve desconsiderar caracteres de espaço.

# ENTRADA:
a = str(input())
b = str(input())

# PROCESSAMENTO:
achou = True
i = 0
while i < len(a) and achou:
    achou = False
    if a[i] != ' ':
        for j in range(len(b)):
            if b[j] != ' ':
                if a[i] == b[j]:
                    achou = True
    i += 1

# SAÍDA:
if achou:
    print(1)
else:
    print(0)