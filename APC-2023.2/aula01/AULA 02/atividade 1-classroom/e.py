# E) Faça um programa que indique se um número que o usuário digitou é divisível por 4 e por 7 ao mesmo tempo mas não divisível por 5.

num = int(input('Informe um número: '))

if num % 4 == 0 and num % 7 == 0 and num % 5 != 0:
    print(f'O número: {num} é divisível por 4 e 7 ao mesmo tempo. Mas não é divisível por 5.')
else:
    print('Tente novamente!')