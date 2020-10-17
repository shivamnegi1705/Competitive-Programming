# Question Link:- https://atcoder.jp/contests/abc180/tasks/abc180_d

x,y,a,b = list(map(int,input().split()))

ans = 0
while x<y:
    diff = x*a - x
    if diff<=b:
        x = x*a
        if x<y:
            ans+=1
    else:
        if y-1-x>=b:
            diff = y-1-x
            diff = diff//b
            ans+=diff
        break
print(ans)
