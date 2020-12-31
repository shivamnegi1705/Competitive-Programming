# Question Link:- https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x = ['a','e','i','o','u']
        y = ['A','E','I','O','U']
        v = 0
        u = 0
        for i in s[:len(s)//2]:
            if i in x or i in y:
                v+=1
        for i in s[len(s)//2::]:
            if i in x or i in y:
                u+=1
        if v==u:
            return True
        return False
