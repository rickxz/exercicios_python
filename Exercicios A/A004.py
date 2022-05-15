# Faça um programa que leia o nome de um(a) aluno(a). 
# Após isso, o programa deve ler duas notas de provas. 
# O programa deve calcular da média simples delas e escrever a saída conforme modelo abaixo. 
# A média deve ser escrita com duas casas decimais.

# ENTRADA: 
nome = str(input())
nota1 = float(input())
nota2 = float(input())

# PROCESSAMENTO: 
media = (nota1 + nota2)/2

# SAÍDA: 
print('{} obteve {:.2f} de media'.format(nome, media))
# print(f'{nome} obteve {media:.2f} de media.') ---> maneira alternativa