# D) Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.

# // = divisao inteira
# % = o resto 

segundos = int(input('Informe os segundos: '))

dia = 86400
hora = 3600
minutos = 60

quant_dia = segundos // dia
segundos = segundos % dia
quant_hora = segundos // hora
segundos = segundos % hora
quant_minutos = segundos // minutos
segundos = segundos % minutos

print(f'{quant_dia} dias,{quant_hora} horas,{quant_minutos} minutos,{segundos} segundos.')