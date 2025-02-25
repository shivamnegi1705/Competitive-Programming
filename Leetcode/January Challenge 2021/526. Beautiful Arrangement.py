# Question Link:- https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, N):
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)
        return count(N, set(range(1, N + 1)))
