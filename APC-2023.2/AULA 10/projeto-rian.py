import pandas as pd
def verifica_cpf(cpf):
    cpf=str(cpf).replace('-','.').split('.')
    cont=0
    for i in range(len(cpf)):
        if i<=2 and len(cpf[i])==3 or i==3 and len(cpf[i])==2:
          cont+=1
        if cont==4:
           return True 
    return False

lista=[]

arquivo=pd.read_csv('apc.2/csv_projeto/usuarios.csv')

for i in range(len(arquivo['nome'])): 
    if pd.isna(arquivo['cpf'][i]):
        cpf=arquivo['nome'][i]
        problema=f'erro encontrado cpf de {cpf} inexistente linha {i+2}'
        lista.append(problema)
    elif verifica_cpf(arquivo['cpf'][i])==False:
        cpf=arquivo['nome'][i]
        problema=f'erro encontrado cpf de {cpf} invalido linha {i+2}'
        lista.append(problema)
    if pd.isna(arquivo['matricula'][i]):
        matricula=arquivo['nome'][i]
        problema=f'erro encontrado matricula de {matricula} inexistente linha {i+2}'
        lista.append(problema)
# print(lista)

for j in lista :
    print(j)