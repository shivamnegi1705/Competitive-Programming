class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dp = [[0 for i in range(target+1)]for j in range(d)]
        for i in range(1,min(target+1,f+1)):
            dp[0][i] = 1
        
        for i in range(1,d):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if j-k>0:
                        dp[i][j] = (dp[i][j]+dp[i-1][j-k])%mod
        return dp[d-1][target]
