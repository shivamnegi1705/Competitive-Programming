# Question Link:- https://atcoder.jp/contests/abc181/tasks/abc181_c

from math import atan2

def func(arr,n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and k!=i:
                    m1 = atan2((arr[i][1]-arr[j][1]),(arr[i][0]-arr[j][0]))
                    m2 = atan2((arr[i][1]-arr[k][1]),(arr[i][0]-arr[k][0]))
                    m3 = atan2((arr[k][1]-arr[j][1]),(arr[k][0]-arr[j][0]))
                    if m1==m2 and m2==m3:
                        return True
    return False
                    
n = int(input())
pts = []
for i in range(n):
    x,y = list(map(int,input().split()))
    pts.append([x,y])
if (func(pts,n))==True:
    print("Yes")
else:
    print("No")
