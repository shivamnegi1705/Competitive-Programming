# Question Link:- https://codeforces.com/contest/1433/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    one = False
    cnt = 0
    for i in range(n):
        if arr[i]:
            one = True
            ans+=cnt
            cnt = 0
        else:
            if one:
                cnt+=1
    print(ans)
