from sklearn.linear_model import LinearRegression
import numpy as np

m,n = map(int, input().strip().split())
x, y = [], []
for i in range(n):
    data = list(map(float, input().strip().split()))
    x.append(data[:-1])
    y.append(data[-1])
    
reg = LinearRegression()
reg.fit(x,y)

a = reg.intercept_
b = reg.coef_
 
q = int(input()) 
 
for j in range(q):
    data = list(map(float,input().strip().split()))
    y = a + np.dot(data, b) 
    print(round(y,2))