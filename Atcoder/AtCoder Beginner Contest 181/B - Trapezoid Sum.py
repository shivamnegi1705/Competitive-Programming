# Question Link:- https://atcoder.jp/contests/abc181/tasks/abc181_b

def func(n):
    x = n*(n+1)
    return x//2
ans = 0
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    a = func(x)
    b = func(y)
    ans+=(b-a)+x
print(ans)
