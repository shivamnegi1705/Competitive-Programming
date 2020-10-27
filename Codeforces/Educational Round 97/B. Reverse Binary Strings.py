# Question Link:- https://codeforces.com/contest/1437/problem/B

for _ in range(int(input())):
    n = int(input())
    s = input()
    x = '10'*(n//2)
    y = '01'*(n//2)
    a = 0
    b = 0
    cnt = 0 
    # print(x,y)
    for i in range(n):
        if s[i]!=x[i]:
            cnt+=1
        else:
            if cnt!=0:
                cnt = 0
                a+=1
    if cnt!=0:
        a+=1
    cnt = 0
    for i in range(n):
        if s[i]!=y[i]:
            cnt+=1
        else:
            if cnt!=0:
                cnt = 0
                b+=1
    if cnt!=0:
        b+=1
    print(min(a,b))
