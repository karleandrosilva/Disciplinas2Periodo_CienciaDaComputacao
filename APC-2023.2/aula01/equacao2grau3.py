# DESVIO CONDICIONAL - DESAFIO 2

a = int(input('informe o primeiro número: '))
b = int(input('informe o segundo número: '))
c = int(input('informe o terceiro número: '))
delta = (b**2) - (4 * a * c)

if delta > 0:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print('o valor de x1 é: ', x1)
    print('o valor de x2 é: ', x2)
elif delta == 0:
    raiz = (-b / (2 * a))
    print('Como o delta é igual a zero, significa que a equação tem uma única raiz que é: ', raiz)
else:
    print('Não da para calcular as raízes, tente novamente!')