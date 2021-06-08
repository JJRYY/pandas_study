import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)

list_index = [1, 2, 3, 4, 5]
sr2 = pd.Series(list_data, index=list_index)
idx2 = sr2.index
val2 = sr2.values
print(idx2)
print('\n')
print(val2)
print("sr2[4] >> ", sr2[4])