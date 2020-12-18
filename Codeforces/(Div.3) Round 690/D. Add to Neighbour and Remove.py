# Question Link:- https://codeforces.com/contest/1462/problem/D

inf = 10**5
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = n-1
    pre = 0
    for i in range(n):
        pre+=arr[i]
        m = i
        s = 0
        l = i+1
        for j in range(i+1,n):
            s+=arr[j]
            if s>pre:
                m+=inf
            elif s==pre:
                s = 0
                m+=(j-l)
                l = j+1
        if s>0:
            m+=inf
        ans = min(ans,m)
    print(ans)
