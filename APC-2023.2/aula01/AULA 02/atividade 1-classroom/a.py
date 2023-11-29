# A) Escreva um program que recebe 3 notas de prova e calcula:
# - A media delas;
# - A media ponderada delas, considerando pesos 2, 2 e 3.
#- A média ponderada delas, considerando pesos 1, 2 e 2.

valor1 = float(input('Informe sua primeira nota: '))
valor2 = float(input('Informe sua segunda nota: '))
valor3 = float(input('Informe sua terceira nota: '))

calcular_media = (valor1 + valor2 + valor3) / 3
calcular_ponderada1 = (valor1 * 2 + valor2 * 2 + valor3 * 3) / 7 
calcular_ponderada2 = (valor1 * 1 + valor2 * 2 + valor3 * 2 ) / 5

print(f'A sua média: {calcular_media:.2f}\nA sua média ponderoda do primeiro exemplo: {calcular_ponderada1:.2f}\nA sau média ponderada do segundo exemplo: {calcular_ponderada2:.2f}')