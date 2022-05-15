# Faça um programa que leia dois números inteiros. 
# Após isso, seu programa deve imprimir o resultado das seguintes operações: 
# 1) o valor da divisão real do primeiro número lido pelo segundo (imprimir com duas casas decimais); 
# 2) o valor da divisão inteira do primeiro pelo segundo (imprimir como número inteiro); 
# 3) o valor do resto da divisão do primeiro pelo segundo (imprimir como número inteiro).

# ENTRADA:
n1 = int(input())
n2 = int(input())

# PROCESSAMENTO:
divisao_real = n1/n2 # Símbolo de divisão real: /
divisao_inteira = n1//n2 # Símbolo de divisão inteira: //
resto = n1%n2 # Símbolo do resto: %

# SAÍDA:
print(f'{divisao_real:.2f}')
print(f'{divisao_inteira}')
print(f'{resto}')