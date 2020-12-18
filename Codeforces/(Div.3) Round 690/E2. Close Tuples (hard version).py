# Question Link:- https://codeforces.com/contest/1462/problem/E2

mod = 10**9+7
mex = 200005
fact = [1]
for i in range(1,mex):
    fact.append((fact[-1]*i)%mod)
def func(n,r):
    if n<r:
        return 0
    t = fact[n]
    a,b = fact[r],fact[n-r]
    d = (a*b)%mod
    d = pow(d,mod-2,mod)
    return (t*d)%mod

for _ in range(int(input())):
    n,m,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = [-1]+arr
    cnt = [0 for i in range(n+1)]
    for i in range(1,n+1):
        cnt[arr[i]]+=1
    for i in range(1,n+1):
        cnt[i]+=cnt[i-1]
    ans = 0
    for i in range(1,n+1):
        if cnt[i]==0:
            continue
        r = i+k
        r = min(r,n)
        h = cnt[r]-cnt[i-1]
        ans = (ans+func(h,m))%mod
        h = cnt[r]-cnt[i]
        ans = (ans-func(h,m))%mod

    print(ans)
