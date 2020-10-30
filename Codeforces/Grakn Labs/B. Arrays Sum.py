# Question Link:- https://codeforces.com/contest/1408/problem/B

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    temp = [arr[i] for i in range(n)]
    last = [0 for i in range(n)]
    cnt = 0
    while arr!=last:
        mex = arr[0]
        uni = 1
        arr[0] = 0
        for i in range(1,n):
            if arr[i]==mex:
                arr[i] = 0
            else:
                if uni<k:
                    mex = arr[i]
                    uni+=1
                    arr[i] = 0
                else:
                    arr[i]-=mex
        cnt+=1
        if arr==temp:
            cnt = -1
            break
        else:
            temp = [arr[i] for i in range(n)]
    print(cnt)
