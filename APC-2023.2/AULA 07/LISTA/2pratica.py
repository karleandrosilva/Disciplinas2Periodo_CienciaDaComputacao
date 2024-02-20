# lista [] podem ser modificadas.

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)


# ADICIONAR

lanche.append('cookies') #adicionou no final da lista
print(lanche)

lanche.insert(0,'hotdog') # adiciona na posicão que deseja == ex -> 0
print(lanche)


# REMOVER

lanche.pop() # remove o último item da lista
print(lanche)

lanche.pop(2) # remove o item que deseja pelo índice
print(lanche)

del lanche[3] # remove o item que deseja pelo índice
print(lanche)

lanche.remove('pizza') # remove o item que deseja pelo conteudo.
print(lanche)