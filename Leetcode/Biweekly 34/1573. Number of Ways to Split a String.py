# Question Link:- https://leetcode.com/problems/number-of-ways-to-split-a-string

class Solution:
    def numWays(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        
        if s.count('0')==n:
            x = ((n-1)*(n-2))%mod
            p = pow(2,mod-2,mod)
            return (x*p)%mod
        
        cnt = 0
        for i in range(n):
            if s[i]=='1':
                cnt+=1
        if cnt%3!=0:
            return 0
        
        c = 0
        a,b = 0,0
        for i in range(n):
            if s[i]=='1':
                c+=1
            if c==(cnt//3) and s[i]!='1':
                a+=1
        
        c = 0
        for i in range(n):
            if s[i]=='1':
                c+=1
            if c==2*(cnt//3) and s[i]!='1':
                b+=1
        return ((a+1)*(b+1))%mod
            
            
                
