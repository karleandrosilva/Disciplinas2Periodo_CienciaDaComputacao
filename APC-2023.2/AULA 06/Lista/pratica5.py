numeros = [-80, 0, -80, 12, 24, 77, -33, 0, -80, 1, 2, 2, 2, 3, 2]
cont = 0
numero = int(input('informe um número: '))

for i in numeros:
    if i == numero:
        cont += 1

print(cont)