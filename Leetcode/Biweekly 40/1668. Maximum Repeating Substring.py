# Question Link:- https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        mex = 0
        for i in range(1,100):
            if word*i in sequence:
                mex = max(mex,i)
        return mex
