# 9. Luigi ganhou uma mochila nova com capacidade para transportar até 18 kg. Como tem muitos livros, ele deseja descobrir quantos podem ser levados na mochila sem exceder esse limite. Escreva um programa que receba como entrada o peso de vários livros de Luigi e exiba a quantidade de livros que podem ser carregados.
# Dica: A entrada deve parar quando um novo livro exceder a capacidade da mochila.

capacidade = 18
peso_livros = 0
cont = quant = 0

while peso_livros <= capacidade:
    quant = quant + 1
    peso_livros = int(input(f'Luigi insira o peso do livro {cont+1}: '))
    capacidade = capacidade - peso_livros
    cont = cont + 1
    peso_livros = 0

print(f'Só podem ser carregados {quant} livros!')