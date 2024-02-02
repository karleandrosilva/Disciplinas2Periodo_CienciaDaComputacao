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


def fatorial (x):
    if x == 0 or x == 1:
        return 1
    else:
        return mult(x, fatorial(x-1))


def exponenciacao (x,y):
    if y == 0:
        return 1
    else:
        return (mult(x, exponenciacao(x, y-1)))


def fibonacci (x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    

num =  int(input('Informe um número: '))

print(sucessorDeUmNumero(num))
  
print(sucessorDeUmNumero(soma(5,8)))

print(mult(2,3))

print(fatorial(3))

print(exponenciacao(2, 3))

print(fibonacci(5))