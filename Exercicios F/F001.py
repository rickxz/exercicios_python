# Faça um programa que leia as dimensões N e M de uma matriz A, 
# representando o número de linhas e colunas respectivamente. 
# Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A. 
# Por fim, imprima a matriz em formato matricial.

# ENTRADA:
n, m = input().split()
n, m = int(n), int(m)
valores = input().split()

# PROCESSAMENTO:
a = []
indice_valor = i = j = 0
while i < n:
    linha = []
    j = 0
    while j < m:
        linha.append(int(valores[indice_valor]))
        indice_valor += 1
        j += 1
    a.append(linha)
    i += 1

# SAÍDA:
i = 0
while i < n:
    j = 0
    while j < m:
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1