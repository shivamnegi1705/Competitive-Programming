# Question Link:- https://codeforces.com/contest/1435/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = arr[::]
    ans = ans[-1::-1]
    for i in range(n//2):
        ans[i] = -ans[i]
    print(*ans)
