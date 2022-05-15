# Faça um programa que leia os coeficientes a, b e c de uma equação do segundo grau ax² + bx + c.
# Após isso, calcule e imprima a soma das raízes da equação. Se as raízes não forem reais, imprima nan (use print(math.nan))

import math

# ENTRADA:
a = float(input())
b = float(input())
c = float(input())

# PROCESSAMENTO:
delta = b**2 - 4 * a * c

if delta < 0:
    print(math.nan)
else:
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f'{x1 + x2:.2f}')