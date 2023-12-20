# 5. Maria acabou de iniciar seu curso de graduação na faculdade de medicina na UFAL e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.
# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho)
# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
coelhos = 0
ratos = 0
sapos = 0
quant_cobaias = int(input('Informe a quantidade de testes: '))

for cont in range(quant_cobaias):
    cobaia = int(input('Informe a quantidade de cobaias: '))
    tipo_cobaia = input('Informe o tipo de cobaia [C/R ou S]: ')
    if tipo_cobaia == 'C':
        coelhos = cobaia + coelhos
    elif tipo_cobaia == 'R':
        ratos = cobaia + ratos
    elif tipo_cobaia == 'S':
        sapos = cobaia + sapos
    else:
        print('tente novamente!')
    
total = coelhos + ratos + sapos 

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')