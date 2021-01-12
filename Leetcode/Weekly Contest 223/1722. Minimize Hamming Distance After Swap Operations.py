# Question Link:- https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        graph = [[] for i in range(n)]
        for i in allowedSwaps:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        vis = [False for i in range(n)]
        ans = 0
        for i in range(n):
            if vis[i]==False:
                vis[i] = True
                q = [i]
                d = {}
                ind = []
                while q!=[]:
                    cur = q[0]
                    q.pop(0)
                    if source[cur] in d:
                        d[source[cur]]+=1
                    else:
                        d[source[cur]] = 1
                    ind.append(cur)
                    for j in graph[cur]:
                        if vis[j]==False:
                            vis[j] = True
                            q.append(j)
                for j in ind:
                    if target[j] in d and d[target[j]]>0:
                        d[target[j]]-=1
                        ans+=1
        return n-ans
