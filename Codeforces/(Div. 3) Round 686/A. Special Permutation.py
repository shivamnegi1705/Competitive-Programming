# Question Link:- https://codeforces.com/contest/1454/problem/A

for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        arr = [i+1 for i in range(n-1,-1,-1)]
        print(*arr)
    else:
        arr = [n]
        for i in range(n-1):
            arr.append(i+1)
        print(*arr)
