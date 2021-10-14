# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a=int(input())
b=int(input())

print(str(int(round(math.degrees(math.atan2(a, b))))) + '°')