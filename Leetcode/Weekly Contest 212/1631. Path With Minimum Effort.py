# Question Link:- https://leetcode.com/problems/path-with-minimum-effort/

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        n,m = len(heights),len(heights[0])
        pq = [[0,[0,0]]]
        dist = [[10**10 for i in range(m)]for j in range(n)]
        dist[0][0] = 0
        heapq.heapify(pq)
        while pq!=[]:
            x,y = pq[0][1]
            pq.pop(0)
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx>=0 and nx<n and ny>=0 and ny<m:
                    d = abs(heights[x][y]-heights[nx][ny])
                    if dist[nx][ny] > max(dist[x][y],d):
                        dist[nx][ny] = max(dist[x][y],d)
                        heapq.heappush(pq,[dist[nx][ny],[nx,ny]])
        return (dist[n-1][m-1])
