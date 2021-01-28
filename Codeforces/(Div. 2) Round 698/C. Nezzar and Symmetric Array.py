# Question Link:- https://codeforces.com/contest/1478/problem/C

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    d = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    f = 0
    for i in d:
        if i%2!=0 or d[i]%2!=0:
            f = 1
    if n==1:
        if f==0:
            print("YES")
        else:
            print("NO")
        continue
    arr.sort()
    val = []
    for i in range(0,2*n,2):
        val.append(arr[i])
    fac = 2*n
    pre = 0
    tot = 0
    ans = set()
    for i in range(n-1,-1,-1):
        cnt = val[i]
        cnt-=tot*2
        if cnt%fac==0 and cnt>=0:
            cnt = cnt//fac
            if cnt!=0:
                ans.add(cnt)
            tot+=cnt
            fac-=2
    if len(ans)==n and f==0:
        print("YES")
    else:
        print("NO")
