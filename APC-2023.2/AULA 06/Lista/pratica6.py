numeros = [-80, 0, -80, 12, 24, 77, -33, 0, -80, 1, 2, 2, 2, 3, 2]
numero = int(input('informe um número: '))
cont = 0
dicionario = {}

for i in numeros:
    if i == numero:
        cont += 1
        dicionario = {i: cont}

if dicionario:
    print(dicionario)
else:
    print('nao existe')