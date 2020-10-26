# Question Link:- https://codeforces.com/contest/1436/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        arr[i][i] = 1
        if i+1<n:
            arr[i][i+1] = 1
    arr[-1][0] = 1
    for i in arr:
        print(*i)
