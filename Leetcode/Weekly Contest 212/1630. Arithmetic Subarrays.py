# Question Link:- https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        ans = []
        for i in range(len(l)):
            arr = []
            for j in range(l[i],r[i]+1):
                arr.append(nums[j])
            arr.sort()
            d = set()
            for j in range(1,len(arr)):
                d.add(arr[j]-arr[j-1])
            if len(d)==1:
                ans.append(True)
            else:
                ans.append(False)
        return ans
