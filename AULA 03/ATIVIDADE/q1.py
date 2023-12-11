# 1. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_da_semana = int(input('Informe um número: '))

if dia_da_semana == 1:
    print('O número que você informou é Domingo.')
elif dia_da_semana == 2:
    print('O número que você informou é Segunda-Feir.')
elif dia_da_semana == 3:
    print('O número que você informou é Terça-Feira.')
elif dia_da_semana == 4:
    print('O número que você informou é Quarta-Feira.')
elif dia_da_semana == 5:
    print('O número que você informou é Quinta-Feira.')
elif dia_da_semana == 6:
    print('O número que você informou é Sexta-Feira.')
elif dia_da_semana == 7:
    print('O número que você informou é Sabádo.')
else:
    print('VALOR INVÁLIDO!')


