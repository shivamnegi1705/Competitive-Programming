# Question Link:- https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        
        # Intuition and Greedy.
        # For each result value at mat[i][j],
        # we greedily take the min(row[i], col[j]).
        # Then we update the row sum and col sum:
        # row[i] -= mat[i][j]
        # col[j] -= mat[i][j]
        
        mat = [[0 for i in range(len(col))]for j in range(len(row))]
        
        for i in range(len(row)):
            for j in range(len(col)):
                mat[i][j] = min(row[i],col[j])
                row[i]-=mat[i][j]
                col[j]-=mat[i][j]
        return mat
