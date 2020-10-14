# Question Link:- https://leetcode.com/problems/make-sum-divisible-by-p/submissions/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # Calculate the need = sum(A) % p.
        # Traverse from L to R, calculate the prefix sum in a map.
        
        # Find the shortest array with sum % p = need.
        # last[remainder] = index records the last index that
        # (A[0] + A[1] + .. + A[i]) % p = remainder
        
        need = sum(nums)%p
        dp = {0:-1}
        cur = 0
        res = n = len(nums)
        for i in range(n):
            a = nums[i]
            cur = (cur+a)%p
            dp[cur] = i
            if (cur-need)%p in dp:
                res = min(res,i-dp[(cur-need)%p])
        if res<n:
            return res
        return -1
