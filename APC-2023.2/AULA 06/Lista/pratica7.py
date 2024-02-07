lista1 = [4, 1, 7, 6, 8, 5]
lista2 = [1, 2, 3, 4, 5, 6]
lista3 = []
cont = 0

if len(lista1) == len(lista2):
    for i in lista1:
        for g in lista2:
            if i == g:
                cont += 1
                lista3.append(i)
                break
            
print(lista3)