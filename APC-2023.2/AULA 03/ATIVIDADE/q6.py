# 6. Faça um programa que peça duas notas e imprima a média informando se o aluno passou ou
# não de ano (Aprovado: nota >=7).

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('VOCÊ FOI APROVADO!')
else:
    print('INFELIZMENTE VOCÊ FOI REPROVADO!')
