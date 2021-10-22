import numpy
l1=[]
l2=[]
M,N= map(int,input().split())
for i in range(M):
    l1.append(input().split())
for i in range(M):
    l2.append(input().split())

a=numpy.array(l1,int)
b=numpy.array(l2,int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a**b)