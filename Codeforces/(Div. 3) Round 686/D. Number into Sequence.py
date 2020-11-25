# Question Link:- https://codeforces.com/contest/1454/problem/D

import math
def func(n):
    ans = []
    d = {}
    while n%2==0:
        if 2 not in d:
            ans.append(2)
            d[2] = 1
        else:
            d[2]+=1
        n = n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            if i not in d:
                ans.append(i)
                d[i] = 1
            else:
                d[i]+=1
            n = n//i
    if n>1:
        ans.append(n)
        d[n] = 1
    ans.sort()
    return [d,ans]
for _ in range(int(input())):
    n = int(input())
    freq,uni = func(n)
    arr = []
    for i in freq:
        arr.append([freq[i],i])
    arr.sort()
    ans = [1 for i in range(arr[-1][0])]
 
    for i in range(len(arr)):
        f,num = arr[i]
        for j in range(f):
            ans[len(ans)-j-1]*=num
    print(len(ans))
    for x in ans:
        print(x,end=' ')
    print()
