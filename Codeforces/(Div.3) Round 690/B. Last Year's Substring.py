# Question Link:- https://codeforces.com/contest/1462/problem/B

for _ in range(int(input())):
    n = int(input())
    s = input()
    f = 0
    if s[n-4]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
        f = 1
    if s[0]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
        f = 1
    if s[0]=='2' and s[1]=='0' and s[n-2]=='2' and s[n-1]=='0':
        f = 1
    if s[0]=='2' and s[1]=='0' and s[2]=='2' and s[n-1]=='0':
        f = 1
    if s[0]=='2' and s[1]=='0' and s[2]=='2' and s[3]=='0':
        f = 1
    if f==1:
        print("YES")
    else:
        print("NO")
    
