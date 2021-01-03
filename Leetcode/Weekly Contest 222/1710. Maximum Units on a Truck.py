# Question Link:- https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, arr: List[List[int]], truckSize: int) -> int:
        n = len(arr)
        for i in range(n):
            arr[i] = [arr[i][1],arr[i][0]]
        arr.sort(reverse=True)
        ans = 0
        for i in range(n):
            p,cnt = arr[i]
            for j in range(cnt):
                if truckSize-1>=0:
                    ans+=p
                    truckSize-=1
        return ans
