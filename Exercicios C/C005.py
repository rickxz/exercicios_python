# Faça um programa que leia uma sequência de números inteiros do usuário até que ele digite o valor zero.
# Quando o valor zero for digitado, o programa deve imprimir o resultado em três linhas:
# 1ª linha) Soma dos valores pares da sequência;
# 2ª linha) Soma dos valores ímpares da sequência;
# 3ª linha) soma de todos os valores da sequência.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
somaPares = 0
somaImpares = 0
soma = 0
while n != 0:
    soma += n
    if n % 2 != 0:
        somaImpares += n
    else:
        somaPares += n
    n = int(input())

# SAÍDA:
print(somaPares)
print(somaImpares)
print(soma)