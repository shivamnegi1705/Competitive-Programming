# Question Link:- https://codeforces.com/contest/1454/problem/C

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    pos = []
    for i in range(n+1):
        pos.append([-1])
    for i in range(n):
        pos[arr[i]].append(i)
    for i in range(0,n+1):
        pos[i].append(n)
    ans = 10**10
    for i in range(1,n+1):
        if len(pos[i])<=2:
            continue
        s = 0
        for j in range(1,len(pos[i])):
            if pos[i][j]-pos[i][j-1]-1>0:
                s+=1
        ans = min(ans,s)
    print(ans)
