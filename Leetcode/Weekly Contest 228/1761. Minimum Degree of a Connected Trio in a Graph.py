# Question Link:- https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        dp = [[0 for i in range(n)]for j in range(n)]
        deg = [0 for i in range(n)]
        for i in edges:
            x,y = i
            x-=1
            y-=1
            dp[x][y] = 1
            dp[y][x] = 1
            deg[x]+=1
            deg[y]+=1
        ans = 10**18
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if dp[i][j]==1 and dp[j][k]==1 and dp[i][k]==1:
                        ans = min(ans,deg[i]+deg[j]+deg[k]-6)
        if ans==10**18:
            return -1
        return ans
