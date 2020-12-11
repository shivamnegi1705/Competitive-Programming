# Question Link:- https://codeforces.com/contest/1461/problem/A

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    s = ['a' for i in range(n)]
    for i in range(k,n):
        s[i] = chr(97+(i-k+1)%3)
    print(''.join(s))
