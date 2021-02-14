# Question Link:- https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = ''
        k = ''
        p = 0
        for i in range(n):
            if p==0:
                t+='0'
            else:
                t+='1'
            p = p^1
        p = 0
        for i in range(n):
            if p==0:
                k+='1'
            else:
                k+='0'
            p = p^1
        cnt = 0
        c = 0
        ans = 10**10
        for i in range(n):
            if s[i]!=t[i]:
                cnt+=1
            if s[i]!=k[i]:
                c+=1
        return min(cnt,c)
            
