lista = []
cont = 0
for c in range(10):
    somador = 0
    for n in range(0, 4):
        nota = float(input(f'Informe a nota {n+1}: '))
        somador += nota
    media = somador / 4
    lista.append(media)
    if media >= 7:
        cont += 1

print(lista)
print(f'A quantidade de médias maior que 7 é: {cont}')