# Question Link:- https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ''
        while k>0:
            for i in range(1,27):
                if i+(n-1)*26>=k:
                    k-=i
                    n-=1
                    s+=(chr(i-1+97))
                    break
        return s
