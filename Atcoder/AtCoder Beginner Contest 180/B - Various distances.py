# Question Link:- https://atcoder.jp/contests/abc180/tasks/abc180_b

n = int(input())
arr = list(map(int,input().split()))
md = 0
for i in arr:
    md+=abs(i)
print(md)
ed = 0
for i in arr:
    ed+=(i**2)
print(ed**(0.5))
cd  = 0
for i in arr:
    cd = max(cd,abs(i))
print(cd)
