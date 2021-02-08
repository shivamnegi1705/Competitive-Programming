# Question Link:- https://leetcode.com/contest/biweekly-contest-45/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, A):
        return max(accumulate(A, initial=0)) - min(accumulate(A, initial=0))
