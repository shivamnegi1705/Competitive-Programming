# Question Link:- https://codeforces.com/contest/1433/problem/C

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    f = True
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            f = False
    if f==True:
        print(-1)
    else:
        mex = max(arr)
        pos = -1
        for i in range(n):
            if arr[i]==mex:
                if i-1>=0 and arr[i-1]!=mex:
                    pos = i
                if i+1<n and arr[i+1]!=mex:
                    pos = i
        print(pos+1)
