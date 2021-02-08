# Question Link:- https://leetcode.com/contest/biweekly-contest-45/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        ans = 0
        for i in d:
            if d[i]==1:
                ans+=i
        return ans
