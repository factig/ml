import pandas as pd
churn=pd.read_csv(r'abalone.csv')
churn.head()
#check missing values
churn.info()
churn.isnull().sum()
churn1=pd.get_dummies(churn,columns=['Sex'],drop_first=True)
print("\n",churn1)
                      
cat_col=['Sex','Height']
churn_final=pd.get_dummies(churn,columns=cat_col,drop_first=True)
print("\n",churn_final)

Y=churn_final[['Rings']]
X=churn_final.drop(columns=['Rings'])

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=12345)
print(f'Xtrain={len(X_train)}, Xtest={len(X_test)}, Ytrain={len(Y_train)}, Ytest={len(Y_test)}')

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3,p=2)
model=knn.fit(X_train,Y_train)
Y_test.head()

Y_test['predicted']=model.predict(X_test)
print(Y_test)

from sklearn.metrics import accuracy_score,classification_report
print(accuracy_score(Y_test['Rings'],Y_test['predicted']))
print(classification_report(Y_test['Rings'],Y_test['predicted']))
