def soma (x,y):
    return (x + y)

def subtracao (x,y):
    return (x - y)

def multiplicacao (x,y):
    return (x * y)

def divisao (x,y):
    return (x / y)

def exponenciacao (x,y):
    return (x ** y)

def fatorialA (x):
    if x == 0 or x == 1:
        return 1
    else:
        return(x * fatorialA(x-1))
    
def fatorialB (y):
    if y == 0 or y == 1:
        return 1
    else:
        return(y * fatorialB(y-1))
    

calculadora = True
while calculadora == True:
    a = int(input('Informe um número: '))
    b = int(input('Informe um número: '))

    operacao = int(input(f'''
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTILPICAÇÃO   
[ 4 ] DIVISÃO 
[ 5 ] EXPONENCIAÇÃO
[ 6 ] FATORIAL
Informe qual operação você deseja fazer com {a} e {b}: '''))
    
    if operacao == 1:
        print(f'A SOMA É: {soma(a,b)}')
    elif operacao == 2:
        print(f'A SUBTRAÇÃO É: {subtracao(a,b)}')
    elif operacao == 3:
        print(f'A MULTIPLICAÇÃO É: {multiplicacao(a,b)}')
    elif operacao == 4:
        print(f'A DIVISAÕ É: {divisao(a,b)}')
    elif operacao == 5:
        print(f'A EXPONENNCIAÇÃO É: {exponenciacao(a,b)}')
    elif operacao == 6:
        print(f'O FATORIAL DE {a} É: {fatorialA(a)} E O FATORIAL DE {b} É: {fatorialB(b)}')

    continuar = input('''
Deseja continuar? Se sim, digite: S
Caso nao, Informe: N
Insira sua resposta: [S/N]: 
''')
    
    if continuar == 'S' or continuar == 's':
        continue
    elif continuar == 'N' or continuar == 'n':
        calculadora = False