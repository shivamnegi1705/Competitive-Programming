# Question Link:- https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = [[] for i in range(10**5)]
        self.graph[0].append(kingName)
        self.level = {}
        self.level[kingName] = 0
        self.edges = {self.king:[]}
    
    def birth(self, parentName: str, childName: str) -> None:
        self.level[childName] = self.level[parentName]+1
        self.graph[self.level[childName]].append(childName)
        if parentName in self.edges:
            self.edges[parentName].append(childName)
            if childName not in self.edges:
                self.edges[childName] = []
        else:
            if childName not in self.edges:
                self.edges[childName] = []
            self.edges[parentName] = [childName]

    def death(self, name: str) -> None:
        lvl = self.level[name]
        self.graph[lvl].remove(name)
        del self.level[name]
        
    def getInheritanceOrder(self) -> List[str]:
        
        ans = []
        def dfs(cur,parent=-1):
            nonlocal ans
            if cur in self.level:
                ans.append(cur)
            for i in self.edges[cur]:
                if i!=parent:
                    dfs(i,cur)
        dfs(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
