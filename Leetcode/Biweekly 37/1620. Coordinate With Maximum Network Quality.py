# Question Link:- https://leetcode.com/problems/coordinate-with-maximum-network-quality/

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        ans = [1000,1000]
        best = -10**10
        for i in range(101):
            for j in range(101):
                me = 0
                for k in towers:
                    d2 = (i-k[0])**2 + (j-k[1])**2
                    if d2<=radius*radius:
                        qual = (k[2]//(1+(d2**0.5)))
                        me+=qual
                if best<me:
                    best = me
                    ans = [i,j]
                elif best==me:
                    l = [ans,[i,j]]
                    l.sort()
                    ans = l[0]
        return ans
