# 8. Faça um programa que peça um número e imprima se ele é par ou ímpar.

numero = int(input('Informe um número: '))

if numero // 2:
    print(f'O número {numero} que você inseriu, é PAR!')
else:
    print(f'O número {numero} que você inseriu, é ÍMPAR!')