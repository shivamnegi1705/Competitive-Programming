# Question Link:- https://leetcode.com/contest/weekly-contest-176/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # traversing the whole matrix to count number of negative numbers.
        # We can also use binary search in this ques.
        n,m = len(grid),len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]<0:
                    ans+=1
        return ans
