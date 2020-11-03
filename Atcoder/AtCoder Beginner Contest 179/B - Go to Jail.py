# Question Link:- https://atcoder.jp/contests/abc179/tasks/abc179_b

n = int(input())
arr = []
for i in range(n):
    x,y = list(map(int,input().split()))
    arr.append([x,y])
f = 0
cnt = 0
for i in arr:
    if i[0]==i[1]:
        cnt+=1
        if cnt==3:
            f = 1
    else:
        cnt = 0
if f==1:
    print("Yes")
else:
    print("No")
