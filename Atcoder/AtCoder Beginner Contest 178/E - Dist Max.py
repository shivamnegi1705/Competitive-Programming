# Question Link:- https://atcoder.jp/contests/abc178/tasks/abc178_e

def func(x, y):
    res, n = 0, len(x)
    for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
        smallest = p * x[0] + q * y[0] + 0
        for i in range(n):
            cur = p * x[i] + q * y[i]
            res = max(res, cur - smallest)
            smallest = min(smallest, cur)
    return res

n = int(input())
x,y = [],[]
for i in range(n):
    a,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)
print(func(x,y))
