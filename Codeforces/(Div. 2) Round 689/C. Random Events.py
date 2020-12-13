# Question Link:- https://codeforces.com/contest/1461/problem/C

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    req = n
    for i in range(n-1,-1,-1):
        if arr[i]==i+1:
            req = i
        else:
            break
    ans = 0
    p = 1
    for i in range(m):
        x,y = list(map(float,input().split()))
        x = int(x)
        if x>=req:
            ans+=(p*y)
            p = p*(1-y)
    if req==0:
        ans = 1
    print(ans)
