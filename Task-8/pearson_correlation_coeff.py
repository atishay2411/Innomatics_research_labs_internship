from math import *

data_size = int(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

X_mean = sum(X) / data_size
X_std = sqrt(sum([(i-X_mean)**2 for i in X]) / data_size)

Y_mean = sum(Y) / data_size
Y_std = sqrt(sum([(i-Y_mean)**2 for i in Y]) / data_size)

correlation = 0

for i,j in zip(X,Y):
    correlation += ((i - X_mean) * (j - Y_mean)) / (data_size * X_std * Y_std)


print(round(correlation, 3))