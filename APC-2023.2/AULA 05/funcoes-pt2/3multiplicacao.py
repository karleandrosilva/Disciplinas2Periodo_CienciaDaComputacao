def sucessorDeUmNumero (num):
    return  num + 1


def soma(x, y):
    if (x == 0):
        return y
    else:
        return sucessorDeUmNumero(soma(x-1, y))


def mult(x, y):
    if x == 0:
        return 0
    else:
        return soma(y, mult(x-1, y))
    

num =  int(input('Informe um número: '))

print(sucessorDeUmNumero(num))
  
print(sucessorDeUmNumero(soma(5,8)))

print(mult(2,3))