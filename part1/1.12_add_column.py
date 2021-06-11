import pandas as pd

exam_data = {
    '이름' : ['서준', '우현', '인아'],
    '수학' : [90, 80, 70],
    '영어' : [98, 89, 95],
    '음악' : [85, 95, 100],
    '체육' : [100, 90, 90]
}
df = pd.DataFrame(exam_data)
print(df, end='\n\n')

df['국어'] = [80, 90, 100]
print(df, sep='\n', end='\n\n')

df['평균'] = round(df.mean(axis=1), 2)
df['총점'] = df.sum(axis=1)

print(df, sep='\n', end='\n\n')