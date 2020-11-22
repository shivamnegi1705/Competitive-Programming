# Question Link:- https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        arr = []
        n = len(tasks)
        for i in range(n):
            diff = tasks[i][1]-tasks[i][0]
            arr.append([diff,tasks[i][1],tasks[i][0]])
        arr.sort(reverse=True)
        
        def func(m):
            for i in range(n):
                if m>=arr[i][1]:
                    m-=arr[i][2]
                else:
                    return False
            return True
        lo = 1
        hi = 10**12
        while lo<hi:
            mid = (lo+hi)//2
            x = func(mid)
            if x==True:
                hi = mid
            else:
                lo = mid
            if hi-lo==1:
                break
        if func(lo)==True:
            return lo
        return hi
