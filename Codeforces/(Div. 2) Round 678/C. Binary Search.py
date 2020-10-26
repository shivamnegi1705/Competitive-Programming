# Question Link:- https://codeforces.com/contest/1436/problem/C

n,x,pos = list(map(int,input().split()))
lo = 0
hi = n
greater = n-x
smaller = x-1
ans = 1
mod = (10**9)+7
while lo<hi:
    mid = (lo+hi)//2
    if mid<pos:
        ans = (ans*smaller)%mod
        smaller-=1
        lo = mid+1
    elif mid==pos:
        lo = mid+1
    else:
        ans = (ans*greater)%mod
        greater-=1
        hi = mid
left = smaller+greater
for i in range(1,left+1):
    ans = (ans*i)%mod
print(ans)
