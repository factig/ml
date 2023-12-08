import pandas as pd

data={'NAME': ['Sam','Kia','Jack','Lilly','Riya','Keshav','Rose'],
      'AGE': [12,13,14,13,12,14,13],
      'Gender':['M','F','M','F','F','M','F'],
      'Marks': [98,76,'NaN',65,74,'NaN',66]}
df=pd.DataFrame(data)
print(df)

print('\n')
print(df.isnull().sum)
print('\n')
print(df.info())
print('\n')
print(df.describe)

c=avg=0
for ele in df['Marks']:
    if str(ele).isnumeric():
        c+=1
        avg+=ele
avg/=c
print('\n')
print(f'Average:{avg}')
print('\nAfter Replacing missing values:\n')

df=df.replace(to_replace='NaN',value=avg)
print(df)

df['Gender']=df['Gender'].map({'M':'Male',
                               'F':'Female',}).astype('string')
print('\nCategorising Gender:\n')
print(df)

df=df[df['Marks']>=75]
print('\nTop Scorers:\n')
print(df)

df=df.drop(['AGE'],axis=1)
print('\nAfter removing Age column:\n',df)

data1=pd.DataFrame({'NAME': ['Sam','Kia','Jack','Lilly','Riya','Keshav','Rose'],
                   'AGE': [12,13,14,13,12,14,13],
                   'Gender':['M','F','M','F','F','M','F'],
                   'Marks': [98,76,'NaN',65,74,'NaN',66],
                   'ID':[101,103,105,107,104,109,122]})
                   
data2=pd.DataFrame({'ID':[101,103,105,107,104,109,122],
                    'Fee Status':[2340,'Nil',600,876,7800,'Nil',987]})
print('\n',data2)

h=pd.merge(data1,data2,on="ID")
print(f'\nAfter merging the dataframe: {h}')

grouped=data1.groupby('AGE')
print('\n',grouped.get_group(13))

