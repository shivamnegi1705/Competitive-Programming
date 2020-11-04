# Question Link:- https://atcoder.jp/contests/abc177/tasks/abc177_b

ans = 10**10
s = input()
n = len(s)
t = input()
m = len(t)
for i in range(n-m+1):
    cnt = 0
    for j in range(m):
        if s[i+j]!=t[j]:
            cnt+=1
    ans = min(ans,cnt)
print(ans)
