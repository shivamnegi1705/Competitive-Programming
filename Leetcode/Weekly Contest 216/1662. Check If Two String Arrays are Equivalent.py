# Question Link:- https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ''
        for i in word1:
            s+=i
        t = ''
        for i in word2:
            t+=i
        if s==t:
            return True
        return False
        
