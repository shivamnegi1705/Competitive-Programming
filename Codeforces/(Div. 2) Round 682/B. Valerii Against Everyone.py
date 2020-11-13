# Question Link:- https://codeforces.com/contest/1438/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    f = 0
    for i in d:
        if d[i]>1:
            f = 1
    if f==0:
        print("NO")
    else:
        print("YES")
