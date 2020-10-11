# Question Link:- https://leetcode.com/problems/maximal-network-rank/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        # array to store degree of nodes of te graph
        deg = [0 for i in range(n)]
        # map to store bidirectional edges.
        edge = {}
        
        # For each edge update degree of nodes and map them in edges dictionary
        for i in roads:
            x,y = i
            deg[x]+=1
            deg[y]+=1
            edge[(x,y)] = 1
            edge[(y,x)] = 1
        
        # mex --> to store max ans
        mex = 0
        # Check all possible pairs
        for i in range(n):
            for j in range(i+1,n):
                # f--> to check if there is a edge between them
                f = 0
                if (i,j) in edge:
                    f =1 
                # Update ans
                mex = max(mex,deg[i]+deg[j]-f)
        return mex
