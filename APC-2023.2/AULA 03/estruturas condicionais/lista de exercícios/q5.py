# 5. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um número: '))

if numero >= 0:
    print(f'O NÚMERO: {numero} É POSITIVO!')
elif numero < 0:
    print(f'O NÚMERO: {numero} É NEGATIVO!')