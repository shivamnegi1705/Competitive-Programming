# Question Link:- https://atcoder.jp/contests/abc186/tasks/abc186_d

n = int(input())
arr = list(map(int,input().split()))
ans = 0
arr.sort()
s = sum(arr)

for i in range(n):
	s-=arr[i]
	ans+=(s-arr[i]*(n-i-1))
print(ans)
