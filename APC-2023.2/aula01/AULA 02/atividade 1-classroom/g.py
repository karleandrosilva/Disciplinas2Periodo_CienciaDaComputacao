# G) Dados três números em ponto flutuante queremos saber quantos deles estão acima da média aritmética.

a = float(input('Informe o primeiro número: '))
b = float(input('Informe o segundo número: '))
c = float(input('Informe o terceiro número: '))

media = (a + b + c) / 3
print(f'A média é: {media:.2f}')

if a > media and b > media and b > media:
    print(f'O número {a}, {b} e {c} estão acima da média')
elif a > media:
    print(f'O número {a} está acima da média')
elif b > media:
    print(f'O número {b} está acima da média')
elif c > media:
    print(f'O número {c} está acima da média')
else:
    print('Tente novamente')




