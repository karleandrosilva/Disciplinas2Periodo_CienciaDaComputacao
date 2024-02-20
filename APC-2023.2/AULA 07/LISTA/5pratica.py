valores = []

for contador in range(0, 5):
    valores.append(int(input('Digite um valor: '))) 

for c in range(len(valores)):
    print(f'Na posião {c+1} encontrei o valor {valores[c]}')