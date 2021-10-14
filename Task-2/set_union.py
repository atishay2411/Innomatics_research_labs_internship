a=int(input())
s1=set(input().split(" "))
b=int(input())
s2=set(input().split(" "))

s3=s1.union(s2)
print(len(s3))