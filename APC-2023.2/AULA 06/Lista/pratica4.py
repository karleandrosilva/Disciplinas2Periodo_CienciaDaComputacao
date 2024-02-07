numeros = [-80, -80, 12, 24, 77, -33, 0, -80, 1, 2, 2, 2, 3, 2]
negativo = True

for i in numeros:
    if i >= 0:
        negativo = False
        break
    
if negativo:
    print('tem')
else:
    print('não tem')




