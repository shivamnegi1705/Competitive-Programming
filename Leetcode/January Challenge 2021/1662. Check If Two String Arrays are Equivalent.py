# Question Link:- https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ''
        w = ''
        for i in word1:
            s+=i
        for i in word2:
            w+=i
        return s==w
