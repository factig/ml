import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('cars.csv')
print(df.head(), '\n\n')
print(df.isnull().sum(), '\n\n')

df_numeric = df.select_dtypes(include=[np.number])
#Heatmap
plt.figure(figsize=(15, 8))
plt.title("Heatmap showing Correlation between all the features", fontsize=20)
sns.heatmap(df_numeric.corr(), annot=True, cmap='mako')
plt.show()
    
#Standard Scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(df_numeric)
df_scaled = pd.DataFrame(scaled, columns=df_numeric.columns)
print(df_scaled.head(), '\n\n')

#Scatter Plots
zero_class = df[df.type == 0]
print('Zero Class:', zero_class.shape, '\n\n')
one_class = df[df.type == 1]
print('One Class:', one_class.shape, '\n\n')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.scatter(zero_class['price'], zero_class['sales'], color='green', marker='+')
plt.scatter(one_class['price'], one_class['sales'], color='red', marker='.')
plt.show()

x = df_scaled
y = df['type']
#SVM
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc=SVC() 
svc.fit(x_train, y_train)
y_pred=svc.predict(x_test)
print('Model accuracy : {0:0.3f}'. format(accuracy_score(y_test, y_pred)), '\n\n')

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])
sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='mako')
plt.title('Confusion Matrix')
plt.show()

#Classification Report
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred), '\n\n')
