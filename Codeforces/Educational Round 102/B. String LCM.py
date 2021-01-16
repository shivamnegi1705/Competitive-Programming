# Question Link:- https://codeforces.com/contest/1473/problem/B

from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
for _ in range(int(input())):
    a = input()
    n = len(a)
    b = input()
    m = len(b)
    l = lcm(n,m)
    t1 = l//n
    t2 = l//m
    if a*t1 == b*t2:
        print(a*t1)
    else:
        print(-1)
