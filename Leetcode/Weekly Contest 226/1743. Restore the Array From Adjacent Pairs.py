# Question Link:- https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mapper = {}
        rev = {}
        cnt = 0
        for i in adjacentPairs:
            x,y = i
            if x not in mapper:
                mapper[x] = cnt
                rev[cnt] = x
                cnt+=1
            if y not in mapper:
                mapper[y] = cnt
                rev[cnt] = y
                cnt+=1
        n = len(mapper)
        deg = [0 for i in range(n)]
        graph = [[] for i in range(n)]
        for i in adjacentPairs:
            x,y = mapper[i[0]],mapper[i[1]]
            deg[x]+=1
            deg[y]+=1
            graph[x].append(y)
            graph[y].append(x)
        st = -1
        for i in range(n):
            if deg[i]==1:
                st = i
        vis = [False for i in range(n)]
        vis[st] = True
        q = [st]
        ans = []
        while q!=[]:
            cur = q[0]
            q.pop(0)
            ans.append(rev[cur])
            for i in graph[cur]:
                if vis[i]==False:
                    vis[i] = True
                    q.append(i)
        return ans
