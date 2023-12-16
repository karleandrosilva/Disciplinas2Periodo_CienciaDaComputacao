# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

valor = 0
contador = 0

while valor < 5:
    info = int(input('Informe um número: '))
    valor = valor + 1
    if info % 2 == 0:
        contador = contador + 1
    # else:
    #     continue

if contador <= 1:
    print(f'{contador} valor par.')
else:
    print(f'{contador} valores pares.')