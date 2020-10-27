# Question Link:- https://codeforces.com/contest/1437/problem/A

for _ in range(int(input())):
    l,r = list(map(int,input().split()))
    if r+1<=2*l:
        print("YES")
    else:
        print("NO")
