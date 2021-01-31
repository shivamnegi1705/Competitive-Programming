# Question Link:- https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False for i in range(n)]for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
        for i in range(3,n):
            c = i-1
            r = 0
            for j in range(n-i+1):
                if dp[r+1][c-1]==True and s[r]==s[c]:
                    dp[r][c] = True
                r+=1
                c+=1
        for i in range(n):
            for j in range(n-1,-1,-1):
                if j>i:
                    if dp[0][i]==True and dp[i+1][j-1]==True and dp[j][n-1]==True:
                        return True
        return False
