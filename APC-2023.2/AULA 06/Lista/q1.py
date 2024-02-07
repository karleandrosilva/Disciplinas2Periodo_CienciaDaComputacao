# Escreva um programa que receba vários números do usuário e armazena em uma lista
# até que o usuário digite um valor menor do que zero. Em seguida, o programa pede ao
# usuário que informe um outro número e escreva uma mensagem informando se esse
# número pertence ou não à lista informada.

numeros = []

while True:
    numero_digitado = int(input('Informe um número: '))
    if numero_digitado == 0:
        break
    numeros.append(numero_digitado)

print(numeros)

numero_lista = int(input('Informe outro número, para verificar se está na lista: '))
if numero_lista in numeros:
    print(f'O {numero_lista} pertence a lista: {numeros}')
else:
    print(f'O {numero_lista} não pertence a lista: {numeros}')