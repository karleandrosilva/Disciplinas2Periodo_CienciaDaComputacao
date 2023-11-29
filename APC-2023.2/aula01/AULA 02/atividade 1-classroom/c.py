# C) O cardápio de uma lanchonete é dado abaixo. 
#Prepare um algoritmo que leia a quantidade de cada item da tabela respectivamente e calcule a conta final.
# Hambúrguer................. R$ 3,00
# Cheeseburger .............. R$ 2,50
# Fritas............................ R$ 2,50
# Refrigerante ................. R$ 1,00
# Milkshake..................... R$ 3,00

print('''Seja bem vindo a nossa Lanchonete!

Hambúrguer................. R$ 3,00
Cheeseburger .............. R$ 2,50
Fritas..................... R$ 2,50
Refrigerante .............. R$ 1,00
Milkshake.................. R$ 3,00

Informe a quantidade de cada item que você irá querer.
Caso não queira algum item, é só preecher 0.''' )

hamburguer = float(input('Informe quantos Hambúrgues: '))  
cheeseburger = float(input('Informe quantos Cheeseburger: '))
fritas = float(input('Informe quantas Fritas: '))
refrigerante = float(input('Informe quantos Refrigerantes: '))
milkshake = float(input('Informe quantos Milkshake: '))

valor_hamburguer = 3.00
valor_cheesburger = 2.50
valor_fritas = 2.50
valor_refrigerante = 1.00
valor_milshake = 3.00

conta_final = (hamburguer * valor_hamburguer) + (cheeseburger * valor_cheesburger) + (fritas * valor_fritas) + (refrigerante * valor_refrigerante) + (milkshake * valor_milshake)

print(f'A conta final foi de R${conta_final}')