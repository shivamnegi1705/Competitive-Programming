# Question Link:- https://codeforces.com/contest/1478/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    d = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans = max(ans,d[i])
    print(ans)
