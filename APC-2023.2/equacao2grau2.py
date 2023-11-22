# DESVIO CONDICIONAL

a = int(input('informe o primeiro número: '))
b = int(input('informe o segundo número: '))
c = int(input('informe o terceiro número: '))
delta = (b**2) - (4 * a * c)
x1 = (-b + delta) / (2 * a)
x2 = (-b - delta) / (2 * a)

if delta < 0:
    print('Não da para calcular as raízes, tente novamente!')
else:
    print('o valor de x1 é: ', x1)
    print('o valor de x2 é: ', x2)