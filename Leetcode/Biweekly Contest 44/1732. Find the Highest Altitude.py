# Question Link:- https://leetcode.com/problems/find-the-highest-altitude/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        arr = []
        for i in gain:
            arr.append(cur)
            cur+=i
        arr.append(cur)
        return max(arr)
