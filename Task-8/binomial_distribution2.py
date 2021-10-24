from math import *

def binomial_dist(x, n, p):
    b = (factorial(n)/(factorial(x)*factorial(n-x))) * (p**x) * ((1-p)**(n-x))
    return b
    
if __name__ == '__main__':
    perc, piston_size = map(float, input().strip().split())
    n , p = 10 , perc/100
    b_dist = sum([binomial_dist(i, n, p) for i in range(3)])
    b_dist2 = sum([binomial_dist(i, n, p) for i in range(2,11)])

    print(round(b_dist, 3))
    print(round(b_dist2, 3))