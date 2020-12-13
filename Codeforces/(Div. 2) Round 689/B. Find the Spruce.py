# Question Link:- https://codeforces.com/contest/1461/problem/B

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    mat = []
    ans = 0
    for i in range(n):
        s = input()
        mat.append(list(s))
    cnt = [[0 for i in range(m)]for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if mat[i][j]=='*':
                cnt[i][j] = 1
    
    for i in range(n):
        for j in range(1,m):
            cnt[i][j]+=cnt[i][j-1]
    
    for i in range(n):
        for j in range(m):
            if mat[i][j]=='*':
                for k in range(1,n+1):
                    x = i+k-1
                    if x>=n:
                        break
                    l = j-k+1
                    r = j+k-1
                    l = max(l,0)
                    r = min(r,m-1)
                    temp = cnt[x][r]
                    if l>0:
                        temp-=cnt[x][l-1]
                    if temp==2*k-1:
                        ans+=1
                    else:
                        break
    print(ans)
