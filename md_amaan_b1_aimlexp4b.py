import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head(5),"\n\n")

df2 = df[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare']]
print(df2.head(5),"\n\n")

print(df2.info(),"\n\n")
print(df2.isnull().sum(),"\n\n")

updated_df1=df2.dropna(axis=0)
print(updated_df1.info())

print('\nSkew:',df2['Age'].skew())

updated_df3=df2
updated_df3['Age']=updated_df3['Age'].fillna(updated_df3['Age'].mean())
print('\n',updated_df3.info())

"""fare=df['Fare']
arr=fare.to_numpy()
print(np.mean(arr))
print(np.median(arr))
plt.boxplot(arr,vert=False)
plt.show()
"""
sample= [15,18, 29, 45, 34, 12, 13, 14, 90]
mean= np.mean(sample)
print('\nMean: ',mean)

median= np.median(sample)
print('\nMedian: ',median)

plt.boxplot(sample, vert=False)
plt.show()

print('sample: ',sample)
print('Q2 quantile of sampe: ',np.median(sample))
print('Q1 quantile of sampe: ',np.quantile(sample,.25))
print('Q3 quantile of sampe: ',np.quantile(sample,.75))
