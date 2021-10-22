import numpy
ls1=[]
ls2=[]
N=int(input())
for i in range(N):
    ls1.append(list(map(int,input().split())))
for i in range(N):
    ls2.append(list(map(int,input().split())))    
    
arr1=numpy.array(ls1)
arr2=numpy.array(ls2)

print(numpy.dot(arr1, arr2)) 