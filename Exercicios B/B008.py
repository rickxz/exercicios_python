# Faça um programa que leia três números inteiros A, B e C e imprima o maior deles.

# ENTRADA:
a = int(input())
b = int(input())
c = int(input())

# PROCESSAMENTO:
if (a > b):
    if (a > c):
        print(a)
    else:
        print(c)

if (b > a):
    if (b > c):
        print(b)
    else:
        print(c)