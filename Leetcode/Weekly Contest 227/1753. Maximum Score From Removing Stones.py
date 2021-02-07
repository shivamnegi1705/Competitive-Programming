# Question Link:- https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [-a,-b,-c]
        heapq.heapify(arr)
        ans = 0
        while len(arr)>1:
            x = -heapq.heappop(arr)
            y = -heapq.heappop(arr)
            z = min(x,y)
            if z>0:
                ans+=1
            if x!=0:
                heapq.heappush(arr,-(x-1))
            if y!=0:
                heapq.heappush(arr,-(y-1))
        return ans
