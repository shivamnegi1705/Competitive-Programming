# Question Link:- https://codeforces.com/contest/1473/problem/C

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    if n==k:
        ans = [i+1 for i in range(k)]
        print(*ans)
    else:
        t = 2*k-n-1
        ans = [i+1 for i in range(t)]
        temp = []
        for i in range(t,k):
            temp.append(i+1)
        temp.sort(reverse=True)
        ans+=temp
        print(*ans)
