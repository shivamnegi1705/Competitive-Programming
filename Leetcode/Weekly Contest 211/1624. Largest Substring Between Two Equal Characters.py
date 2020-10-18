# Question Link:- https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        mex = 0
        f = 0
        for i in range(n):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    f = 1
                    x = j-i+1-2
                    mex = max(mex,x)
        if f==0:
            return -1
        return mex
