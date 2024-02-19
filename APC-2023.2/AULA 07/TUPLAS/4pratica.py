lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'Eu comi {len(lanche)} coisas!')

print('-'*20)

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posicão {contador}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')