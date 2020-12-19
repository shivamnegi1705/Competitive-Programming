# Question Link:- https://atcoder.jp/contests/abc186/tasks/abc186_c

n = int(input())
ans = 0
for i in range(1,n+1):
	x = str(i)
	f = 0
	if '7' in x:
		continue
	y = oct(i)
	if '7' in y:
		continue
	ans+=1
print(ans)
