# Question Link:- https://codeforces.com/contest/1421/problem/A

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    x = a&b
    print((x^a) + (x^b))
