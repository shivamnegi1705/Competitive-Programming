# Question Link:- https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        ans = [-1 for i in range(n+1)]
        if n<=1:
            return n
        ans[0] = 0
        ans[1] = 1
        i = 1
        while i<=n:
            x = 2*i
            if x>=2 and x<=n:
                ans[x] = ans[i]
            if x+1>=2 and x+1<=n:
                ans[x+1] = ans[i]+ans[i+1]
            i+=1
        return max(ans)
