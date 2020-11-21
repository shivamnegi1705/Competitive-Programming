# Question Link:- https://codeforces.com/contest/1451/problem/A

for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(0)
    elif n==2:
        print(1)
    elif n==3:
        print(2)
    else:
        if n%2==0:
            print(2)
        else:
            print(3)
