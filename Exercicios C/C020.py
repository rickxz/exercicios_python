# Faça um programa que leia um conjunto de valores que correspondem as idades de pessoas de uma comunidade.
# Quando o valor fornecido for um número negativo, significa que não existem mais idades para serem lidas.
# Após a leitura, seu programa deve informar:

# A média das idades das pessoas (com duas casas decimais)
# A quantidade de pessoas maiores de idade
# A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) (com duas casas decimais)

# ENTRADA:

idade = int(input())

# PROCESSAMENTO:
quantia = 0
soma_idades = 0
maioridade = 0
idosos = 0
while idade >= 0:
    soma_idades += idade
    quantia += 1
    if idade >= 18:
        maioridade += 1
        if idade > 75:
            idosos += 1
    idade = int(input())

# SAÍDA:
print(f'{soma_idades/quantia:.2f}')
print(f'{maioridade}')
print(f'{idosos/quantia * 100:.2f}%')