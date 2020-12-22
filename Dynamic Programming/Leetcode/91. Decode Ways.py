# Question Link:- https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        if s[0]!='0':
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(2,n+1):
            last = s[i-1]
            if int(last)>0:
                dp[i]+=dp[i-1]
            duo = s[i-2]+s[i-1]
            if int(duo)>=10 and int(duo)<=26:
                dp[i]+=dp[i-2]
        return dp[n]
