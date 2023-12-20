'''Escreva um programa calculadora que efetua operações entre dois números inteiros fornecidos pelo usuário.
Alguns requisitos:
operações: soma, subtração, divisão, multiplicação, fatorial e exponenciação.
as operações fatorial e exponenciação devem ser implementadas usando a multiplicação.
o usuário deve poder efetuar quantas operações desejar sem que o programa finalize.
o programa só deve finalizar quando o usuário desejar.'''

while True:
    numero1 = int(input('Informe um número: '))
    numero2 = int(input('Informe outro número: '))

    opcao = int(input(f'''Com os números: {numero1} e {numero2}. Qual operação você deseja fazer:
    [ 1 ] SOMA
    [ 2 ] SUBTRAÇÃO
    [ 3 ] DIVISÃO
    [ 4 ] MULTIPLICAÇÃO
    [ 5 ] FATORAÇÃO
    [ 6 ] EXPONENCIAÇÃO '''))
    if opcao == 1:
        resposta = numero1 + numero2
    elif opcao == 2:
        resposta = numero1 - numero2
    elif opcao == 3:
        resposta = numero1 // numero2
    elif opcao == 4:
        resposta = numero1 * numero2
    elif opcao == 5:
        numero_fatorial = int(input('Informe o número que você quer o fatorial: '))
        if numero_fatorial == 0 and numero_fatorial == 1:
            resposta = 1
        else:
            fatorial = 1
            for cont in range(numero_fatorial):
                fatorial = fatorial * (cont + 1)
            resposta = fatorial
    elif opcao == 6:
        resposta = numero1 ** numero2

    print(f'A RESPOSTA É: {resposta}')
    
    continuar = 'S'
    while continuar == 'S' or continuar == 'N':
        continuar = input('Você deseja continuar? [S/N]: ')
        if continuar == 'S':
            continue
        elif continuar == 'N':
            False
        else:
            print('Caso queira continuar, digite: Sim.\nSe não, digite: Não.')