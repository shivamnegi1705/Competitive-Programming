# Question Link:- https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        x = ' '
        x = x*len(s)
        if x==s:
            return 1
        n = len(s)
        l,r = 1,n
        def func(m):
            cnt = [0 for i in range(127)]
            for i in range(m):
                x = ord(s[i])
                cnt[x]+=1
            f = 0
            for i in range(127):
                if cnt[i]>1:
                    f = 1
            if f==0:
                return True
            for i in range(m,n):
                x = ord(s[i])
                y = ord(s[i-m])
                cnt[x]+=1
                cnt[y]-=1
                f = 0
                for j in range(127):
                    if cnt[j]>1:
                        f = 1
                if f==0:
                    return True
            return False
        while l<r:
            m = (l+r)//2
            x = func(m)
            if x==True:
                l = m
            else:
                r = m
            if r-l==1:
                break
        if func(r)==True:
            return r
        else:
            return l
            
        
