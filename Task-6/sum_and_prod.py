import numpy
N,M= map(int,input().split())
ls=[]
for i in range(N):
    ls.append(list(map(int,input().split())))
arr=numpy.array(ls)

summation=numpy.sum(arr,axis=0)
print(numpy.prod(summation))

    

