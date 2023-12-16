# 9. O arquivo de entrada contém um valor real qualquer. O programa deve apresentar uma mensagem dizendo em qual dos seguintes intervalos: [0,25] (25,50], (50,75], (75,100]. Se o valor for menor do que 0 ou maior do que 100 deve ser apresentada uma mensagem “Fora de intervalo”.
# Por exemplo:
# ● [0,25] indica valores entre 0 e 25.0000, inclusive eles.
# ● (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000
# ● Ou seja, os símbolos [ e ] são usados para representar o intervalo fechado e os símbolos ( e ) para intervalos abertos.
# Entrada: 25.0200
# Saída: Intervalo (25,50]

valor = float(input('Insira um valor entre 0 e 100: '))

if valor >= 0 and valor < 25:
    print('INTERVALO: [0,25]')

elif valor >= 25 and valor < 50:
    print('INTERVALO: (25,50]')

elif valor >=50 and valor < 75:
    print('INTERVALO: (50,75]')

elif valor >= 75 and valor <= 100:
    print('INTERVALO: (75,100]')

else:
    print('FORA DE INTERVALO!')