# Faça um programa que leia as dimensões N e M de uma matriz A, 
# representando o número de linhas e colunas respectivamente. 
# Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A. 
# Por fim, o programa deve imprimir a soma de cada coluna da matriz.

# ENTRADA:
n, m = input().split()
n, m = int(n), int(m)
valores = input().split()

# PROCESSAMENTO:
a = []
i = indice_valor = 0
while i < n:
    linha = []
    j = 0
    while j < m:
        linha.append(int(valores[indice_valor]))
        indice_valor += 1
        j += 1
    a.append(linha)
    i += 1

j = 0
while j < m:
    i = 0
    soma = 0
    while i < n:
        soma += a[i][j]
        i += 1
    j += 1
    print(soma)