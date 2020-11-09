# Question Link:- https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [0 for i in range(n+1)]
        for i in range(2,n+1):
            p = int(i**0.5)+1
            div = []
            for j in range(1,p):
                if i%j==0:
                    if i//j==j:
                        div.append(j)
                    else:
                        div.append(i//j)
                        div.append(j)
            for j in div:
                if j!=i:
                    val = dp[i-j]
                    if val==0:
                        dp[i] = 1
                        break
        # print(dp)
        if dp[n]==1:
            return True
        else:
            return False
