# Question Link:- https://codeforces.com/contest/1454/problem/B

for _ in range(int(input())):
    n = int(input())
    d = {}
    arr = list(map(int,input().split()))
    uni = list(set(arr))
    uni.sort()
    ans = -1
    cnt = 0
    mapper = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
        mapper[i] = cnt
        cnt+=1
    for i in uni:
        if d[i]==1:
            ans = i
            break
    if ans==-1:
        print(ans)
    else:
        print(mapper[ans]+1)
