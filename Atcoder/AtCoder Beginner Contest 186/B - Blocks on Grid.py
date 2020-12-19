# Question Link:- https://atcoder.jp/contests/abc186/tasks/abc186_b

n,m = list(map(int,input().split()))
mat = []
for i in range(n):
	mat.append(list(map(int,input().split())))
x = 10**10
for i in mat:
	x = min(x,min(i))
ans = 0
for i in mat:
	for j in i:
		ans+=abs(j-x)
print(ans)
