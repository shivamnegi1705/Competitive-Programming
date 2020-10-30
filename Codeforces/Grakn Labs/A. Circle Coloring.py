# Question Link:- https://codeforces.com/contest/1408/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    crr = list(map(int,input().split()))
    ans = [-1 for i in range(n)]
    ans[0] = arr[0]
    for i in range(1,n-1):
        if arr[i]!=ans[i-1]:
            ans[i] = arr[i]
        elif brr[i]!=ans[i-1]:
            ans[i] = brr[i]
        else:
            ans[i] = crr[i]
    if arr[n-1]!=ans[n-2] and arr[n-1]!=ans[0]:
        ans[n-1] = arr[n-1]
    elif brr[n-1]!=ans[n-2] and brr[n-1]!=ans[0]:
        ans[n-1]=brr[n-1]
    else:
        ans[n-1] = crr[n-1]
    print(*ans)
