# Question Link:- https://atcoder.jp/contests/abc184/tasks/abc184_b

n,x = list(map(int,input().split()))
s = input()
for i in s:
    if i=='o':
        x+=1
    else:
        x-=1
        x = max(x,0)
print(x)
