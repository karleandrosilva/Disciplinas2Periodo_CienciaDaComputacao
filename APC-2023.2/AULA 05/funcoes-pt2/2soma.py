# FUNÇÃO PARA SABER A SOMA DE UM NÚMERO

def sucessorDeUmNumero (num):
    return  num + 1


def soma(x, y):
    if (x == 0):
        return y
    else:
        return sucessorDeUmNumero(soma(x-1, y))


num =  int(input('Informe um número: '))

print(sucessorDeUmNumero(num))

print(sucessorDeUmNumero(soma(5,5)))                  