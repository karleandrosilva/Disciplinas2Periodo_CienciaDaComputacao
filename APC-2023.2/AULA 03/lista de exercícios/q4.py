# 4. Faça um programa que peça dois números e imprima o maior deles.

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

if numero1 > numero2:
    print(f'O VALOR: {numero1}. É O MAIOR NÚMERO!')

elif numero2 > numero1:
    print(f'O VALOR: {numero2}. É O MAIOR NÚMERO!')

else:
    print(f'OS VALORES: {numero1} e {numero2}. SÃO IGUAIS!')