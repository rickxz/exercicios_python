# Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento da população de coelhos através de uma sequência
# de números naturais que passou a ser conhecida como Sequência de Fibonacci.
# O n-ésimo número da sequência de Fibonacci Fn é dado pela seguinte formula: Fi = Fi-1 + Fi-2.
# O resultado é a sequência {1, 1, 2, 3, 5, 8, 13, 21, ...}.

# Faça um programa que leia um número inteiro positivo N e imprima os N primeiros números da sequência de Fibonacci, todos em uma linha separados por espaço.

# ENTRADA:
n = int(input())

# PROCESSAMENTO:
i = 0
ultimo = 1
penultimo = 1
while i < n:
    if i < 2:
        print(1, end = ' ')
    else:
        atual = ultimo + penultimo
        print(atual, end = ' ')
        ultimo = penultimo
        penultimo = atual
    i += 1

