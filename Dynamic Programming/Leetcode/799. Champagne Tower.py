# Question Link:- https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, n: int, r: int, qg: int) -> float:
        prev = [n]
        for i in range(1,r+1):
            arr = [0 for i in range(i+1)]
            for j in range(len(prev)):
                if prev[j]>1:
                    arr[j]+=(prev[j]-1)/2
                    arr[j+1]+=(prev[j]-1)/2
            prev = arr[::]
        return min(prev[qg],1)
