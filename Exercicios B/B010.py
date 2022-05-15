# Sejam A, B e C os três lados de um triângulo. Faça um programa que leia o valor de três lados de um triângulo A, B e C.
# Seu algoritmo deve informar se o triangulo é: Escaleno (todos os lados diferentes); Isósceles (possui dois lados iguais); e Equilátero (todos os lados iguais);
# Não forma triângulo (quando a soma de dois lados é menor que o terceiro lado).

a = float(input())
b = float(input())
c = float(input())

if (a + b < c) or (a + c < b) or (b + c < a):
    print('INVALIDO')
elif a == b and a == c:
    print('EQUILATERO')
elif (a == b and a != c) or (a == c and b != c) or (b == c and a != c):
    print('ISOSCELES')
else:
    print('ESCALENO')