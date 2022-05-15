# Faça um programa que leia um valor inteiro N. 
# Após isso, leia N valores inteiros colocando-os em uma lista. 
# Em seguida, seu programa deve trocar os elementos dos índices adjacentes, par a par. 
# Por exemplo, deve ser trocado o elemento do índice 0 com o do índice 1, 
# em seguida o elemento do índice 2 com o do índice 3 e assim sucessivamente. 
# Por fim, seu programa deve imprimir a lista resultante.

# ENTRADA:
n = int(input())
numeros = input().split()

# PROCESSAMENTO:
i = primeiro = proximo = 0
while i < len(numeros) - 1: # 5 6 3 8 2 0
    primeiro = numeros[i]
    proximo = numeros[i + 1]
    numeros[i + 1] = primeiro
    numeros[i] = proximo
    i += 2


# SAÍDA:
i = 0
while i < len(numeros):
    print(int(numeros[i]), end = ' ')
    i += 1