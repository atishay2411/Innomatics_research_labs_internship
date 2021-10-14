# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())

isstrictsuperset = True

for i in range(N):
    s = set(map(int, input().split()))
    if not s.issubset(A):
        isstrictsuperset = False
    if len(s) >= len(A):
        isstrictsuperset = False

print(isstrictsuperset)      
