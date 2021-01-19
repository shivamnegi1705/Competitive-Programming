# Question Link:- https://codeforces.com/contest/1474/problem/A

for _ in range(int(input())):
    n = int(input())
    s = input()
    prev = -1
    ans = ''
    for i in range(n):
        d = int(s[i])
        if d==0:
            if prev==1:
                ans+='0'
                prev = 0
            else:
                ans+='1'
                prev = 1
        else:
            if prev==2:
                ans+='0'
                prev = 1
            else:
                ans+='1'
                prev = 2
    print(ans)
