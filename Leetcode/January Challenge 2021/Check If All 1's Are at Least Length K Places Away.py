# Question Link:- https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i]==1:
                if 1 in d:
                    if i-d[1]<k+1:
                        return False
                    else:
                        d[1] = i
                else:
                    d[1] = i
        return True
