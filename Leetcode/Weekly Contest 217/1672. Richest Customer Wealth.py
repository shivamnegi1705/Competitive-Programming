# Question Link:- https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mex = 0
        for i in accounts:
            mex = max(mex,sum(i))
        return mex
        
