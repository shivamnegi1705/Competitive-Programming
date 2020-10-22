# Question Link:- https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        indeg = [0 for i in range(n)]
        for i in range(len(edges)):
            ok = edges[i]
            op = ok[0]
            po = ok[1]
            graph[op].append(po)
            indeg[po]+=1
        ans = []
        for i in range(n):
            if indeg[i]==0:
                ans.append(i)
        return ans
            
