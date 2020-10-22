# Question Link:- https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        while True:
            zc = 0
            i = 0
            while i<n:
                if nums[i]%2==1:
                    break
                elif nums[i]==0:
                    zc+=1
                i+=1
            if zc==n:
                return res
            if i==n:
                for j in range(n):
                    nums[j] = nums[j]//2
                res+=1
            for j in range(i,n):
                if nums[j]%2==1:
                    nums[j]-=1
                    res+=1
        return res
                
        
