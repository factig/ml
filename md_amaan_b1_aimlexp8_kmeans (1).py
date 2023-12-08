import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore')
sns.set()

mall = pd.read_csv('Mall_Customers.csv')
print(mall.head(),'\n''\n')
mall_df = mall.drop(columns=['CustomerID'])
print(mall_df.head(),'\n''\n')
print(mall_df.info(),'\n''\n')
print('The shape of the mall dataframe is: ', mall_df.shape,'\n''\n')
print(mall_df.isnull().sum(),'\n''\n')
print(mall_df.describe().T,'\n''\n')

sns.scatterplot(data=mall_df, x='Annual Income (k$)', y='Spending Score (1-100)')
plt.title('Scatter Plot: Annual Income vs. Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

sns.histplot(mall_df['Age'], kde=True)
plt.title('Histogram: Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.histplot(mall_df['Annual Income (k$)'], kde=True)
plt.title('Histogram: Annual Income Distribution')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Frequency')
plt.show()

mall_dummy = pd.get_dummies(mall_df, columns=['Gender'], drop_first=True)
print(mall_dummy,'\n''\n')

# K-means clustering
error = []
for k in range(1, 10):
    km = KMeans(n_clusters=k)
    km.fit(mall_dummy)
    error.append(km.inertia_)

# Elbow method plot
fig, ax = plt.subplots(figsize=(12, 5))
ax = sns.lineplot(x=range(1, 10), y=error, marker='o', ax=ax)
ax.set_title("Elbow Method for Optimal Clusters")
ax.set_xlabel("Number of Clusters")
ax.set_ylabel("Error of Clusters")
ax.axvline(5, ls="--", c="red", label='Potential Clusters: 5')
ax.axvline(9, ls="--", c="red", label='Potential Clusters: 9')
plt.legend()
plt.show()

selected_clusters = 5
KMeans_selected = KMeans(n_clusters=selected_clusters, init='k-means++').fit(mall_dummy)
clusters = KMeans_selected.fit_predict(mall_dummy)
mall['Clusters'] = clusters
print(mall,'\n''\n')
print(mall['Clusters'].value_counts(),'\n''\n')
print(mall.groupby('Clusters')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean(),'\n''\n')

sns.scatterplot(data=mall, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Clusters', palette="plasma")
plt.title('Clustered Data: Annual Income vs. Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
