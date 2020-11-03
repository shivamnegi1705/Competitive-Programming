# Question Link:- https://atcoder.jp/contests/abc179/tasks/abc179_c

from collections import defaultdict
n = int(input())
mex = 10**6 +5
lp = [0 for i in range(mex)]
prime = []

def init():
    lp[1] = 1
    for i in range(2,mex):
        if lp[i]==0:
            lp[i] = i
            prime.append(i)
        j = 0
        while j<len(prime) and i*prime[j]<mex:
            lp[i*prime[j]] = prime[j]
            if(i%prime[j]==0):
                break
            j+=1
init()
cnt = 0
for i in range(1,n+1):
    temp = n-i
    me = 1
    freq = defaultdict(int)
    while temp>1:
        freq[lp[temp]]+=1
        temp = temp//lp[temp]
    for x in freq:
        me*=(freq[x]+1)
    cnt+=me
print(cnt-1)
