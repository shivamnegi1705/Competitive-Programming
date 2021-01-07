# Question Link:- https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] = max(dp[i],(i-j)*j,(i-j)*dp[j])
        return (dp[-1])
            
        
