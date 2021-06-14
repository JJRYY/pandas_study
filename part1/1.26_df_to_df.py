import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.tail(), end='\n\n')
print(type(df), end='\n\n')

addition = df + 10
print(addition.tail(), end='\n\n')
print(type(addition))

substraction = addition - df
print(substraction.tail(), end='\n\n')
print(type(substraction))