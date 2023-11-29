# D) Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.

# // = divisao inteira

tempo = float(input('Informe os segundos: '))

dia = 86.400
hora = 3.600
minutos = 60

quant_dia = segundos // dia
segundos = segundos % dia
quant_hora = segundos // hora
segundos = segundos % hora
quant_minutos = segundos // minutos
segundos = segundos % minutos

print(f'{quant_dia},{quant_hora},{quant_minutos},{segundos}')