# Question Link:- https://codeforces.com/contest/1474/problem/B

import bisect
mex = 30000
vis = [False for i in range(mex)]
prime = []
def sieve():
    vis = [True for i in range(mex)]
    vis[0] = vis[1] = False
    for i in range(2,mex):
        if vis[i]:
            prime.append(i)
        j = 0
        while j<len(prime) and i*prime[j]<mex:
            vis[i*prime[j]] = False
            if i%prime[j]==0:
                break
            j+=1
sieve()
for _ in range(int(input())):
    n = int(input())
    num = -1
    i = 0
    while i<len(prime) and num==-1:
        if prime[i]-1>=n:
            num = prime[i]
        i+=1
    lo = 0
    hi = len(prime)-1
    while lo<hi:
        mid = (lo+hi)//2
        if prime[mid]>=num+n:
            hi = mid
        else:
            lo = mid
        if hi-lo==1:
            break
    if prime[lo]>=num+n:
        ano = prime[lo]
    else:
        ano = prime[hi]
    print(num*ano)
