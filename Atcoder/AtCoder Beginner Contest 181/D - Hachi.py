# Question Link:- https://atcoder.jp/contests/abc181/tasks/abc181_d

ans = []
for i in range(100,1001):
    if i%8==0:
        ans.append(i)
s = input()
mp = {}
if len(s)>=3:
    for i in s:
        x = i
        if x in mp:
            mp[x]+=1
        else:
            mp[x] = 1
        g = 0
    for i in ans:
        x = str(i)
        f = 0
        d = {}
        for j in x:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        for j in d:
            if j in mp:
                if mp[j]>=d[j]:
                    pass
                else:
                    f = 1
            else:
                f = 1
        if f==0:
            g = 1
            break
    if g==1:
        print("Yes")
    else:
        print("No")
else:
    for i in s:
        if i in mp:
            mp[i]+=1
        else:
            mp[i] = 1
    ans = []
    for i in range(0,101):
        if i%8==0:
            ans.append(i)
    g = 0
    for i in ans:
        x = str(i)
        f = 0
        d = {}
        for j in x:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        if mp==d:
            g = 1
            break
    if g==1:
        print("Yes")
    else:
        print("No")
    
