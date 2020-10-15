# Question Link:- https://codeforces.com/contest/1430/problem/C

from math import ceil
import heapq
for _ in range(int(input())):
    n = int(input())
    arr = [-i-1 for i in range(n)]
    if n==2:
        print(2)
        print(1,2)
    else:
        heapq.heapify(arr)
        ops = []
        while len(arr)>=2:
            f = -heapq.heappop(arr)
            s = -heapq.heappop(arr)
            x = ceil((f+s)/2)
            heapq.heappush(arr,-x)
            ops.append([f,s])
        ans = -heapq.heappop(arr)
        print(ans)
        for i in ops:
            print(*i)
