import pandas as pd

cpfs = ['000.000.000-00', '111.111.111-11', '222.222.222-22', '333.333.33-33']
matriculas = [1234, 4567, 8878, 9784]
nomes = ['ana maria', 'carla santos', 'joão gomes', 'pedro almeida']
data_de_nascimento = ['20/02/2000', '14/05/2010', '12/12/2005', '18/06/2022']
df = pd.DataFrame({'cpf': cpfs, 'matricula': matriculas, 'nome': nomes, 'data de nascimento': data_de_nascimento})
df.to_csv('dados/registros.csv',index=False)
print(df)