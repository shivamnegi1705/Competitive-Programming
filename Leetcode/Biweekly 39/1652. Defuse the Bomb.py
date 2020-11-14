# Question Link:- https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if k==0:
            for i in range(len(code)):
                ans.append(0)
            return ans
        n = len(code)
        for i in range(n):
            s = 0
            if k>0:
                for j in range(k):
                    s+=code[(i+j+1)%n]
                ans.append(s)
            else:
                for j in range(abs(k)):
                    s+=code[(i-j-1+n)%n]
                ans.append(s)
        return ans
