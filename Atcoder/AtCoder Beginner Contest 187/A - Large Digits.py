# Question Link:- https://atcoder.jp/contests/abc187/tasks/abc187_a

a,b = list(map(str,input().split()))
s,t = 0,0
for i in a:
    s+=int(i)
for i in b:
    t+=int(i)
print(max(s,t))
