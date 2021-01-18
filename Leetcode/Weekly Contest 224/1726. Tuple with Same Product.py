# Question Link:- https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                x = nums[i]*nums[j]
                if x not in d:
                    d[x] = 1
                else:
                    d[x]+=1
        ans = 0
        for i in d:
            if d[i]>1:
                x = d[i]
                ans+=(x*(x-1))*4
        return ans
