numeros = []
numerosIguaisAmedia = []
numerosMenoresAmedia = []
numerosMaioresAmedia = []

print('Informe vários números e caso queira parar, digite: 00')

while True:
    numero = float(input('Informe um número: '))
    if numero != 00:
        numeros.append(numero)
    else:
        break

print(f'Aqui está os números inseridos por você: {numeros}')

for c in numeros:
    soma = c + soma

media = soma / len(numeros)

print(f'Você adicionou {len(numeros)} números, a média é {media}')

for c in numeros:
    if c == media:
        numerosIguaisAmedia.append(c)
    elif c < media:
        numerosMenoresAmedia.append(c)
    else:
        numerosMaioresAmedia.append(c)

if numerosIguaisAmedia == []:
    print('Nao teve nenhum número igual a média.')
else:
    print(f'Aqui está uma ista com os números iguais a média {numerosIguaisAmedia}')

if numerosMenoresAmedia == []:
    print('Nao teve nenhum número menor que a média.')
else:
    print(f'Aqui está uma ista com os números menores que a média {numerosMenoresAmedia}')

if numerosMaioresAmedia == []:
    print('Nao teve nenhum número maior que a média.')
else:
    print(f'Aqui está uma ista com os números maiores que a média {numerosMaioresAmedia}')