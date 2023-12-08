import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('IceCreamData.csv')
print(data.shape)
print("\n",data.head())

X=data['Temperature'].values
Y=data['Revenue'].values

mean_x=np.mean(X)
mean_y=np.mean(Y)
n=len(X)
print("\nNumber of Datapoints: ",n)

numer=0
denom=0
for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
m=numer/denom
c=mean_y-(m*mean_x)
print(f"\nCoefficients: \nSlope:{m} \tY-intercept:{c}")

max_x=np.max(X)+2
min_x=np.min(X)-2
x=np.linspace(min_x,max_x,1000)
y=c+m*x
plt.plot(x,y,color='#58b970',label='Regression Line')
plt.scatter(X,Y,c='#ef5423',label='Scatter Plot')
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.legend()
plt.show()

rmse=0
for i in range(n):
    y_pred=c+m*X[i]
    rmse+=(Y[i]-y_pred)**2
rmse=np.sqrt(rmse/n)
print("\nRMSE: ",rmse)

ss_tot=0
ss_res=0
for i in range(n):
    y_pred=c+m*X[i]
    ss_tot+=(Y[i]-mean_y)**2
    ss_res+=(Y[i]-y_pred)**2
r2=1-(ss_res/ss_tot)
print(f"\nRSS: {ss_res}")
print("\nR2 Score: ",r2)
