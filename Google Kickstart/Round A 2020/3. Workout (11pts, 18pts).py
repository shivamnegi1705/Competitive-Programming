# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b

from math import ceil
for test in range(int(input())):
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    diff = []
    for i in range(1,n):
        diff.append(arr[i]-arr[i-1])
    
    def func(mid):
        cnt = 0
        for i in diff:
            cnt+=ceil(i/mid)-1
        if cnt<=k:
            return True
        else:
            return False
    lo = 1
    hi = 10**10
    while lo<hi:
        mid = (lo+hi)//2
        if func(mid)==True:
            hi = mid
        else:
            lo = mid
        if hi-lo==1:
            break
    if func(lo)==True:
        print("Case #"+str(test+1)+":",lo)
    else:
        print("Case #"+str(test+1)+":",hi)
