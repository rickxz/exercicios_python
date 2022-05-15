# Escrever um programa que, dado um ano qualquer, verifica se ele é bissexto ou não. 
# Seu programa deve escrever como saída o número 1 se o ano for bissexto, e 0 caso contrário. 
# Se o ano for inválido escreva -1.

# São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
# São bissextos todos os múltiplos de 4 e não múltiplos de 100, p.ex: 1996, 2004, 2008, 2012, 2016…
# Não são bissextos todos os demais anos.

# ENTRADA:
ano = int(input())

# PROCESSAMENTO:
if ano <= 0:
    print(-1)
elif ano%400 == 0 or ano %4 == 0 and ano%100 != 0:
    print(1)
else:
    print(0)