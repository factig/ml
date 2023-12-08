from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data=pd.read_csv('IceCreamData.csv')
X=data.iloc[:,0:-1]
Y=data.iloc[:,-1]
print(X)
print("\n",Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,Y_train)

Y_pred=model.predict(X_test)
print("\nPredictions:\n",Y_pred)

print("\nSlope: ",model.coef_)
print("\nIntercept: ",model.intercept_)

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
rmse=np.sqrt(Y_test,Y_pred)
rss=np.sum((Y_test-Y_pred)**2)
r2=r2_score(Y_test,Y_pred)

print("\nRMSE: ",rmse)
print("\nRSS: ",rss)
print("\nR Squared: ",r2)
