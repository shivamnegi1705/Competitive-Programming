# Question Link:- https://atcoder.jp/contests/abc187/tasks/abc187_d

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    x,y = arr[i]
    arr[i] = [2*x+y,x,-y]

arr.sort(reverse=True)

for i in range(n):
    x,y,z = arr[i]
    arr[i] = [y,-z]

a,b = 0,0
for i in range(n):
    a+=arr[i][0]
cnt = 0
b = 0
for i in range(n):
    if b<=a:
        b+=arr[i][0]+arr[i][1]
        a-=arr[i][0]
        cnt+=1
print(cnt)
