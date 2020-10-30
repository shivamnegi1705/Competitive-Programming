# Question Link:- https://codeforces.com/contest/1408/problem/D

n,m = list(map(int,input().split()))
mex = 10**6+5
ans = [0 for i in range(mex)]
robber,searchlight = [],[]

for i in range(n):
    robber.append(list(map(int,input().split())))

for i in range(m):
    searchlight.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        x = searchlight[j][0]-robber[i][0]
        y = searchlight[j][1]-robber[i][1]+1
        if x>=0 and y>=0:
            # right moves ranging from 0 to x requires y up moves
            ans[x] = max(ans[x],y)

for i in range(mex-2,-1,-1):
    ans[i] = max(ans[i+1],ans[i])

cnt = 10**10
for i in range(mex):
    cnt = min(cnt,i+ans[i])

print(cnt)
