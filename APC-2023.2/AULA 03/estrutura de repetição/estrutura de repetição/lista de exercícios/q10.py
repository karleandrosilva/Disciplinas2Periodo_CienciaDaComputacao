# 10.Genival tem muito medo de ter diabetes e, por isso, o médico pediu que ele medisse sua glicose ao longo do dia para ver se ela estava controlada. Escreva um programa que receba como entrada os vários valores da taxa de glicose de Genival, até que o valor informado seja 0, e calcule a glicose média observada naquele dia.
# Caso esse valor seja inferior a 110, o programa deve exibir a mensagem "Glicose Normal". Caso seja 200 ou mais, a mensagem exibida deve ser “Glicose Muito Alta". Nos demais casos, o programa deve exibir “Glicose Alterada”.

taxa_glicose = True

while taxa_glicose == True:
    taxa_glicose = int(input('Informe o valor da taxa de Glicose: '))
    if taxa_glicose > 0 and taxa_glicose < 110:
        print('Glicose Normal')
    elif taxa_glicose >= 200:
        print('Glicose Muito Alta')
    elif taxa_glicose == 0:
        taxa_glicose = False
    else:
        print('Glicose Alterada')
  