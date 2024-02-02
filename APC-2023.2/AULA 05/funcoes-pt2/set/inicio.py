# 1 - usam chaves

frutasVermelhas = {'Morango', 'Maçâ', 'Melancia', 'Framboesa', 'Amora' 'Cereja', 'Acerola'}

print('-'*15)

# 2 - para ver o tamanho usar o (len)

quantFrutas = len(frutasVermelhas)
print(quantFrutas)

print('-'*15)

# 3 - Para ver cada elemento 

for fruta in frutasVermelhas:
    print(fruta)

print('-'*15)

# 4 - Para ver 
frutasAmarelas = ['Abacaxi', 'Banana', 'Melão', 'Maracujá', 'Abacaxi']
print(f'LISTA: {frutasAmarelas}')

frutasSet = set(frutasAmarelas)
print(f'CONJUNTO: {frutasAmarelas}')