# Question Link:- https://atcoder.jp/contests/abc178/tasks/abc178_b

a,b,c,d = list(map(int,input().split()))
ans1 = max(a*c,a*d)
ans2 = max(b*c,b*d)
print(max(ans1,ans2))
