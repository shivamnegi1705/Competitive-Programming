# Question Link:- https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        
        def func(mid,b,l):
            arr = [0]
            for i in range(mid+1):
                if i==0:
                    pass
                else:
                    x = heights[i]-heights[i-1]
                    if x>0:
                        arr.append(x)
            heapq.heapify(arr)
            while len(arr)!=0:
                x = heapq.heappop(arr)
                if b>=x:
                    b-=x
                else:
                    if l>0:
                        l-=1
                    else:
                        return False
            return True
                    
        lo = 0
        hi = n-1
        while lo<hi:
            mid = (lo+hi)//2
            x = func(mid,bricks,ladders)
            if x==True:
                lo = mid
            else:
                hi = mid
            if hi-lo==1:
                break
        if func(hi,bricks,ladders)==True:
            return hi
        else:
            return lo
        
