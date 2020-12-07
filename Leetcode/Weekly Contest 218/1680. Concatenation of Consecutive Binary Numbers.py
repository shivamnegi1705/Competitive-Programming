# Question Link:- https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        size = 0
        result = 0
        mod = 10**9+7
        for i in range(1,n+1):
            if i & (i - 1) == 0:
                size += 1
            result = ((result << size) | i) % mod
        return result
