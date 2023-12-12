# 7. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o
# salário de um colaborador e reajuste-o segundo o seguinte critério: Salários até R$ 280,00
# (incluindo): aumento de 20%. Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%.
# Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%. Salários de R$ 1500,00 em diante
# : aumento de 5%.
# Entrada: 880.50
# Saída: 968.55

salario = float(input('Insira o valor do seu salário: '))

if salario < 280:
    novo_salario = salario + (salario * (20/100))

elif salario >= 280 and salario < 700:
    novo_salario = salario + (salario * (15/100))

elif salario >=700 and salario < 1500:
    novo_salario = salario + (salario * (10/100))

elif salario > 1500:
    novo_salario = salario + (salario * (5/100))

print(f'SEU SALÁRIO SERÁ DE: {novo_salario}')