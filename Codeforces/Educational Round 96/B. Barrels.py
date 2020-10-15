# Question Link:- https://codeforces.com/contest/1430/problem/B


for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    ans = 0
    arr.sort(reverse=True)
    for i in range(k+1):
        ans+=arr[i]
    print(ans)
