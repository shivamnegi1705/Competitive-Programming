# Question Link:- https://codeforces.com/contest/1451/problem/B

for _ in range(int(input())):
    n,q = list(map(int,input().split()))
    s = input()
    for i in range(q):
        l,r = list(map(int,input().split()))
        l-=1
        r-=1
        f = 0
        for i in range(l-1,-1,-1):
            if s[i]==s[l]:
                f = 1
        for i in range(r+1,n):
            if s[i]==s[r]:
                f = 1
        if f==1:
            print("YES")
        else:
            print("NO")
