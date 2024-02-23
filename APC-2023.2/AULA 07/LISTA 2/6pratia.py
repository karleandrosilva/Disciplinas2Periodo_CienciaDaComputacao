galera = []
dado = []

for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # apaga o que tem na lista dado

print(galera)

