a = [2, 3, 4, 7]
b = a[:] # cópia

print(f'A lista A: {a}')
print(f'A lista B: {b}')

b[2] = 8 # na posição 2 será atualizada o 4 para 8

print(f'A lista A: {a}')
print(f'A lista B: {b}') 
