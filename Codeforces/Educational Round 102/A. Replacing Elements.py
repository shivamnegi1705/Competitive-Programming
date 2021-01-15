# Question Link:- https://codeforces.com/contest/1473/problem/A

for _ in range(int(input())):
    n,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[-1]<=d:
        print("YES")
    else:
        x,y = arr[0],arr[1]
        if x+y>d:
            print("NO")
        else:
            for i in range(2,n):
                arr[i] = min(arr[i],x+y)
            arr.sort()
            if arr[-1]<=d:
                print("YES")
            else:
                print("NO")
