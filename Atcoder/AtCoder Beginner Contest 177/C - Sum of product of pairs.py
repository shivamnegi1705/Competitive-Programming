# Question Link:- https://atcoder.jp/contests/abc177/tasks/abc177_c

n = int(input())
arr = list(map(int,input().split()))
mod = 10**9 + 7

s = 0
ans = 0
cur = sum(arr)

for i in range(n):
    s+=arr[i]
    add = cur-s
    ans = (ans+(arr[i]*(add%mod))%mod)%mod
print(ans)
