# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23

for t in range(int(input())):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    ans = {}
    for i in range(n):
        for j in range(n):
            x = i-j
            ans[x] = 0
    for i in range(n):
        for j in range(n):
            x = i-j
            ans[x]+=mat[i][j]
    mex = 0
    for i in ans:
        mex = max(mex,ans[i])
        
    print('Case '+"#"+str(t+1)+":",mex)
