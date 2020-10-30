# Question Link:- https://codeforces.com/contest/1408/problem/C

for _ in range(int(input())):
    n,l = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    lo = 0
    hi = 2*(10**9)
    ans = 0
    eps = 10**(-7)
    while (hi-lo)>eps:
        mid = (lo+hi)/2
        # print(mid)
        x = 0
        t = mid
        pos = 0
        speed = 1
        while t>eps and pos<n:
            dist = arr[pos]-x
            req = dist/speed
            have = min(t,req)
            t-=have
            x+=(have*speed)
            pos+=1
            speed+=1
        if t>eps:
            x+=(t*speed)
        
        y = l
        t = mid
        pos = n-1
        speed = 1
        while t>eps and pos>=0:
            dist = y-arr[pos]
            need = dist/speed
            have = min(t,need)
            t-=have
            y-=(have*speed)
            pos-=1
            speed+=1
        if t>eps:
            y-=(t*speed)
        if x>y:
            hi = mid
        else:
            ans = mid
            lo = mid
    print(ans)
