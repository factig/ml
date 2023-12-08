import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

wine = pd.read_csv(r'winequality-red.csv')

print(wine.head(),'\n')
print(wine.dtypes,'\n\n')

wine['quality'] = wine['quality'].astype('category')
print(wine.dtypes,'\n\n')

print(wine.isnull().sum(),'\n\n')

Y = wine[['quality']]
X = wine.drop(columns=['quality'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1234)

print('X_train=',len(X_train),'\n','X_test=', len(X_test),'\n','Y_train', len(Y_train),'\n','Y_test=', len(Y_test),'\n','\n')

dt = DecisionTreeClassifier()
model = dt.fit(X_train, Y_train.values.ravel())  

Y_test['Pred_quality'] = model.predict(X_test)

print(classification_report(Y_test['quality'], Y_test['Pred_quality'], zero_division=1))

import matplotlib.pyplot as plt
class_names_str = list(map(str, Y['quality'].cat.categories))
plt.figure(figsize=(15, 10))
plot_tree(model, filled=True, feature_names=X.columns.tolist(), class_names=class_names_str)
plt.show()
