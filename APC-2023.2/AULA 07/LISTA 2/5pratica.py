galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(p) # mostra a pessoa -> nome | idade

for p in galera:
    print(p[0]) # mostra o nome da pessoa

for p in galera:
    print(p[1]) # mostra a idade da pessoa

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') # mostra o nome da pessoa