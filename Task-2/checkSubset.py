for i in range(int(input())):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())

    if A.union(B)==B:
        print("True")
    else:
        print("False")