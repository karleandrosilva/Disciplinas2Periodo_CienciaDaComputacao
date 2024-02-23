# 1. Escreva um programa que receba vários números do usuário e armazena em uma lista até que o usuário digite um valor menor do que zero. Em seguida, o programa pede ao usuário que informe um outro número e escreva uma mensagem informando se esse número pertence ou não à lista informada.

def verificar(x, lista):
    for i in lista:
        if i == x:
            return True 
    return False

lista_numeros = []

while True:
    num = int(input('Informe um número: '))
    if num > 0:
        lista_numeros.append(num)
    else:
        break

print(lista_numeros)
outro_num = int(input('Informe outro número: '))
if verificar(outro_num, lista_numeros):
    print('está')
else:
    print('nao está')