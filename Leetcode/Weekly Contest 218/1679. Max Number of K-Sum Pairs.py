# Question Link:- https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in nums:
            if d[i]>0:
                d[i]-=1
                if k-i in d and d[k-i]>0:
                    d[k-i]-=1
                    ans+=1
        return ans
