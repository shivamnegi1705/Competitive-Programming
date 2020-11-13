# Question Link:- https://codeforces.com/contest/1438/problem/C

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    mat = []
    for i in range(n):
        l = list(map(int,input().split()))
        mat.append(l)
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                if mat[i][j]%2!=0:
                    mat[i][j]+=1
            else:
                if mat[i][j]%2==0:
                    mat[i][j]+=1
    for i in mat:
        print(*i)
