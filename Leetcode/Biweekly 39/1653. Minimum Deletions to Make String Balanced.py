# Question Link:- https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 10**10
        n = len(s)
        a = [0 for i in range(n)]
        b = [0 for i in range(n)]
        for i in range(n):
            if s[i]=='a':
                a[i]+=1
            if s[i]=='b':
                b[i]+=1
            if i-1>=0:
                a[i]+=a[i-1]
                b[i]+=b[i-1]
        ans = min(a[n-1],b[n-1])
        for i in range(n):
            x = b[i]
            y = a[n-1]-a[i]
            ans = min(ans,x+y)
        return ans
