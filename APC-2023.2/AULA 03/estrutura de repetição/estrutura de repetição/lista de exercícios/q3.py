# 3. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
# digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar
# em 10, o valor inicial e final devem ser informados também pelo usuário.
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

tabuada = int(input('Montar a tabela do: '))
inicio = int(input('Começa por: '))
termino = int(input('Terminar em: '))

if termino < inicio:
    while True:
        termino = int(input('Informe um valor maior que o inicial: '))
        if termino > inicio:
            break
        else:
            continue

print(f'Vou montar a tabuada do {tabuada} começando em {inicio} e terminando em {termino}: ')

for cont in range(inicio, termino + 1):
    print(f'{tabuada} x {cont} = {tabuada * cont}')