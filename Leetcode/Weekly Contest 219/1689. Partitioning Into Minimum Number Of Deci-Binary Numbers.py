# Question Link:- https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        mex = 0
        for i in str(n):
            mex = max(mex,int(i))
        return mex
        
