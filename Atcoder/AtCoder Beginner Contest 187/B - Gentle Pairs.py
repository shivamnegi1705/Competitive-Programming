# Question Link:- https://atcoder.jp/contests/abc187/tasks/abc187_b

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        xd = arr[j][0]-arr[i][0]
        yd = arr[j][1]-arr[i][1]
        if xd==0:
            continue
        else:
            t = yd/xd
            if t>=-1 and t<=1:
                ans+=1
print(ans)
