import pandas as pd

# df == dataFrame 

alunos = ['ana', 'carlos', 'gilberto', 'marta']
trabalhos = [9,8,7,6]
provas = [9,8,7,6]
seminarios = [9,8,7,6]
artigos = [9,8,7,6]
df = pd.DataFrame({'aluno': alunos,'trabalho': trabalhos, 'prova': provas,
'seminário': seminarios, 'artigo': artigos})
df.to_csv('notas.csv',index=False)
print(df)