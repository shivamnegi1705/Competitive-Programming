# Question Link:- https://atcoder.jp/contests/abc177/tasks/abc177_a

d,t,s = list(map(float,input().split()))
x = d/s
if x<=t:
    print("Yes")
else:
    print("No")
