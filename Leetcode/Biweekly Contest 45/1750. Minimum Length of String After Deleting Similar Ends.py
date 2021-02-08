# Question Link:- https://leetcode.com/contest/biweekly-contest-45/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1
        while i<j and s[i]==s[j]:
            ch = s[i]
            while i<=j and s[i]==ch:
                i+=1
            while i<=j and s[j]==ch:
                j-=1
        if i>j:
            return 0
        else:
            return j-i+1
