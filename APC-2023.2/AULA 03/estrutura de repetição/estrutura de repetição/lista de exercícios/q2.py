# 2. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=120

numero = int(input('Informe um número que você quer saber o fatorial: '))
fatorial = 1

for cont in range(1, numero + 1):
    fatorial = fatorial * cont

print(f'{numero}! = {fatorial}')