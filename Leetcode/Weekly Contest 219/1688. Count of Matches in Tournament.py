# Question Link:- https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n>1:
            nex = 0
            if n%2==0:
                nex = n//2
                ans+=n//2
            else:
                nex = 1+(n-1)//2
                ans+=(n-1)//2
            n = nex
        return ans
        
