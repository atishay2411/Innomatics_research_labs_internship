import numpy
ls=[]
M,N=map(int,input().split())
for i in range(N):
    ls.append(list(map(int,input().split())))

arr=numpy.array(ls)
minimum=numpy.min(arr,axis=1)
print(numpy.max(minimum))
    
    


