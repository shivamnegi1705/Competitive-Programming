# Question Link:- https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # ans will hold max number of transfers such that net value(indegree-outdegree) = 0
        ans = 0
        
        # total number of request (Each request represent one transfer)
        m = len(requests)
        
        # Generating all bitmasks where 1 in each bitmask means we will consider this request.
        for mask in range(1,(2**m)+1):
            
            # indeg will hold net value (indegree-outdegree) of each office
            indeg = [0 for i in range(n)]
            
            # number of on bits in the mask
            onbit = 0
            
            for j in range(m):
                # checking which bit is on.
                if ((mask>>j)&1)==1:
                    # for outdegree -1 and for indegree +1 respective nodes
                    cur = requests[j]
                    indeg[cur[0]]-=1
                    indeg[cur[1]]+=1
                    onbit+=1
                    
            # if all the nodes in the indegree have 0 net value then we will take max ans
            f = 0
            for j in indeg:
                if j!=0:
                    f = 1
            if f==0:
                ans = max(ans,onbit)
        return ans
                
