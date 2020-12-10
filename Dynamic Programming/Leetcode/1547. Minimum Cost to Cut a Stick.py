# Question Link:- https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        dp = [[-1 for i in range(m)]for j in range(m)]
        
        # @lru_cache(None)
        def func(l,r):
            nonlocal dp
            if l+1==r:
                return 0
            if dp[l][r]!=-1:
                return dp[l][r]
            ans = 10**100
            for i in range(l+1,r):
                cost = cuts[r]-cuts[l]
                ans = min(ans,func(l,i)+func(i,r)+cost)
            dp[l][r] = ans
            return ans
        func(0,m-1)
        return (dp[0][-1])
