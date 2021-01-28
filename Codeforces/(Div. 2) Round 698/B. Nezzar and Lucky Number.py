# Question Link:- https://codeforces.com/contest/1478/problem/B

for _ in range(int(input())):
    q,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    ans = [10**18 for i in range(d)]
    x = d
    for i in range(10):
        m = x%d
        if ans[m]==10**18:
            ans[m] = x
        x+=10
    x = 10*d
    for i in range(10):
        m = x%d
        if ans[m]==10**18:
            ans[m] = x
        x+=1
    for i in range(q):
        m = arr[i]%d
        if arr[i]>=ans[m]:
            print("YES")
        else:
            print("NO")
