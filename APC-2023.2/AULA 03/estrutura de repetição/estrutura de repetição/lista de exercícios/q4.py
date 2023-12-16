# 4. Faça um programa que leia 20 valores e imprima a soma dos valores pares e dos
# valores ímpares.

# COM FOR:
soma_pares = 0
soma_impares = 0

for cont in range(20):
    numero = int(input('Informe um valor: '))
    if numero % 2 == 0:
        soma_pares = numero + soma_pares
    else:
        soma_impares = numero + soma_impares

print(f'SOMA DOS PARES: {soma_pares}\nSOMA DOS ÍMPARES: {soma_impares}')

# COM WHILE:
cont = 0
soma_pares = 0
soma_impares = 0

while cont < 20:
    numero = int(input('Informe um valor: '))
    if numero % 2 == 0:
        soma_pares = numero + soma_pares
    else:
        soma_impares = numero + soma_impares
    cont = cont + 1

print(f'SOMA DOS PARES: {soma_pares}\nSOMA DOS ÍMPARES: {soma_impares}')