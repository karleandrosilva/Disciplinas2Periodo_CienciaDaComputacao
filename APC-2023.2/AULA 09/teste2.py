import pandas as pd

A = ['oi', 'olá', 'opa']
B = [7,8,9]
C = [44.6,7.2,3.14]

df = pd.DataFrame({'A': A,'B': B, 'C': C})
print(df)
# df.to_csv('dados/teste3.csv',index=False)
        