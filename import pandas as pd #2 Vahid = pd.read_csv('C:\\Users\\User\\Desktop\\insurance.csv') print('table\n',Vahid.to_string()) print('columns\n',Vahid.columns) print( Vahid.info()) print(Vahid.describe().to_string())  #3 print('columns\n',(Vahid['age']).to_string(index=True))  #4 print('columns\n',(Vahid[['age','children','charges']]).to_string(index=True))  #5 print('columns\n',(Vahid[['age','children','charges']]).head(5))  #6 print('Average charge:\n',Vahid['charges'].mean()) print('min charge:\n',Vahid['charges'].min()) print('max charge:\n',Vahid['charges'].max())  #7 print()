import pandas as pd
#2
Vahid = pd.read_csv('C:\\Users\\User\\Desktop\\insurance.csv')
print('table\n',Vahid.to_string())
print('columns\n',Vahid.columns)
print( Vahid.info())
print(Vahid.describe().to_string())

#3
print('columns\n',(Vahid['age']).to_string(index=True))

#4
print('columns\n',(Vahid[['age','children','charges']]).to_string(index=True))

#5
print('columns\n',(Vahid[['age','children','charges']]).head(5))

#6
print('Average charge:\n',Vahid['charges'].mean())
print('min charge:\n',Vahid['charges'].min())
print('max charge:\n',Vahid['charges'].max())

#7
print()
