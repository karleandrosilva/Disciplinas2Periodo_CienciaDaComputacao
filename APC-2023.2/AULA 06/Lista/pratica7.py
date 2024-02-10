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



if len(lista1) == len(lista2):
    for i in lista1:
        for g in lista2:
            if i == g:
                cont += 1
                lista3.append(i)
                break
            
print(lista3)