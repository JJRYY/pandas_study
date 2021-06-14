import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', len(titanic.columns))
pd.set_option('display.width', 1000)

print("# titanic 데이터셋", type(titanic), titanic.head(), sep='\n', end='\n\n')

df = titanic.loc[:, ['age','fare']]
print(df.head(), end='\n\n')
print(type(df), end='\n\n')

addition = df + 10
print(addition.head(), end='\n\n')
print(type(addition))