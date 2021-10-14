if __name__ == '__main__':
    N = int(input())
    ls=[]
    for i in range(N):
        n=input().split()
        if n[0] == "insert":
            ls.insert(int(n[1]), int(n[2]))
        elif n[0] == "remove":
            ls.remove(int(n[1]))
        elif n[0] == "append":
            ls.append(int(n[1]))
        elif n[0] == "sort":
            ls.sort()
        elif n[0] == "reverse":
            ls.reverse()
        elif n[0] == "pop":
            ls.pop()
        elif n[0] == "print":
            print(ls)
    
