# Question Link:- https://leetcode.com/problems/house-robber/
class Solution:

    def rob(self, nums: List[int]) -> int:

        incl = 0

        excl = 0

        for i in range(len(nums)):

            if excl>incl:

                new_excl = excl

            else:

                new_excl = incl

            incl = excl+nums[i]

            excl = new_excl

        return max(incl,excl)
