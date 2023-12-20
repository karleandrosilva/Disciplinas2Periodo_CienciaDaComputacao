cont = 1
novo_resultado = 0
soma_pesos = 0

while True:
    nota = float(input(f'Insira a nota {cont}: '))
    peso = float(input(f'Insira o peso da nota {cont}: '))

    if nota == 0 and peso == 0:
        break

    else:
        resultado_notaXpeso = nota * peso
        novo_resultado = novo_resultado + resultado_notaXpeso
        soma_pesos += peso
        cont = cont + 1

resultado = novo_resultado / soma_pesos
print(f'{resultado:.2f}')