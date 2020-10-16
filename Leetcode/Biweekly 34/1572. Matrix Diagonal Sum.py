# Question Link:- https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans+=mat[i][i]
        c = n-1
        for i in range(n):
            ans+=mat[i][c]
            c-=1
        if n%2!=0:
            ans-=(mat[n//2][n//2])
        return ans
