# Question Link:- https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        n = len(nums)
        for i in range(n):
            if i%2==0:
                even+=nums[i]
            else:
                odd+=nums[i]
        ans = 0
        podd,peven = 0,0
        for i in range(n):
            x = even-peven
            y = odd-podd
            if i%2==0:
                x-=nums[i]
            else:
                y-=nums[i]
            if podd+x==peven+y:
                ans+=1
            if i%2==0:
                peven+=nums[i]
            else:
                podd+=nums[i]
        return ans
            
        
