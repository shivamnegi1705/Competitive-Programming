# Question Link:- https://atcoder.jp/contests/abc180/tasks/abc180_c

def divisors(n):
    ans = []
    i = 1
    p = int(n**(0.5))
    while i<=p:
        if n%i==0:
            if n//i==i:
                ans.append(i)
            else:
                ans.append(i)
                ans.append(n//i)
        i+=1
    ans.sort()
    return ans
n = int(input())
arr = divisors(n)
for i in arr:
    print(i)
