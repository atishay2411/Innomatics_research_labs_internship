import numpy
N,M= map(int,input().split())
ls=[]
for i in range(N):
    ls.append(list(map(int,input().split())))
arr=numpy.array(ls)


print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr))