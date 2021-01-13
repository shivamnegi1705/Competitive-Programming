#Question Link:- https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ''
        w = ''
        for i in word1:
            s+=i
        for i in word2:
            w+=i
        return s==w
