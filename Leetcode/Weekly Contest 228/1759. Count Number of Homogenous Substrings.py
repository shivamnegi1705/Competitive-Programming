# Question Link:- https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)
        cnt = 1
        ans = 0
        l = 0
        r = 1
        while r<n:
            if s[l]==s[r]:
                cnt+=1
            else:
                ans+=(cnt*(cnt+1))//2
                ans = ans%mod
                l = r
                cnt = 1
            r+=1
        ans+=(cnt*(cnt+1))//2
        ans = ans%mod
        return ans%mod
