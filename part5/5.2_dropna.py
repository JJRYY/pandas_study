import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 16)
pd.set_option('display.width', 600)

print("# for 반복문으로 각 열의 NaN 개수 계산하기")

missing_df = df.isnull()

print("missing_df.columns", missing_df.columns, sep='\n', end='\n\n')
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()  # 각 열의 NaN 개수 파악
    try:
        print(col, ':', missing_count[True])    # NaN 값이 있으면 개수를 출력
    except:
        print(col, ':', 0)  # NaN 값이 없으면 0개 출력

print()

print("# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)")
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns, '\n')

print("# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)")
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))