# Question Link:- https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        glo = nums[0]
        for i in range(1,len(nums)):
            cur = max(nums[i],nums[i]+cur)
            if glo<cur:
                glo = cur
        return glo
        
