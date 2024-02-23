lista1 = [4, 1, 7, 6, 8, 5]
lista2 = [1, 2, 3, 4, 5, 6]
contem = []
cntAnB = []
cntBnA = []

for l in lista1:
    for v in lista2:
        if l == v:
            contem.append(l)

for v in lista2:
    if v not in contem:
        cntAnB.append(v)

for m in lista1:
    if m not in contem:
        cntBnA.append(m)

PEB = (len(contem) / len(lista1)) * 100
PEA = (len(contem) / len(lista2)) * 100

print(f'{PEB}% de A em B\n{PEA}% de B em A.')
print(f'Contem nas duas listas: {contem}\nContem em A e nao em B: {cntAnB}\n Contem B e não em A: {cntBnA}')