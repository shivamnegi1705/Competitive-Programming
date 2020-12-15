# Question Link:- https://codeforces.com/contest/1462/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = [0 for i in range(n)]
    l,r = 0,n-1
    t = 0
    i = 0
    while l<=r:
        if t%2==0:
            ans[i] = arr[l]
            l+=1
        else:
            ans[i] = arr[r]
            r-=1
        t = t^1
        i+=1
    print(*ans)
