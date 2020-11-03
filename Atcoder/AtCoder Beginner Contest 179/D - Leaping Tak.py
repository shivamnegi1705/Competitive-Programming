# Question Link:- https://atcoder.jp/contests/abc179/tasks/abc179_d

n,k = list(map(int,input().split()))
arr = []
for i in range(k):
    l = list(map(int,input().split()))
    arr.append(l)
mex = 2*pow(10,5) + 5
mod = 998244353
dp = [0 for i in range(mex)]
suf = [0 for i in range(mex)]
dp[n] = 1
suf[n] = 1
for i in range(n-1,0,-1):
    for j in range(k):
        l = i+arr[j][0]
        r = i+arr[j][1]
        r = min(r,n)
        if l<=r:
            dp[i] = (dp[i]+suf[l]-suf[r+1])%mod
    suf[i] = (dp[i]+suf[i+1])%mod
print(dp[1])
