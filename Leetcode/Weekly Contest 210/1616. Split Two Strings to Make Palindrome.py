# Question Link:- https://leetcode.com/problems/split-two-strings-to-make-palindrome/submissions/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # Length of given string.
        n = len(a)
        
        # maximum size palindrome centered around center of string a
        ma = 0
        st = (n//2)-1
        if n%2==0:
            en = st+1
        else:
            en = st+2
        while st>=0:
            if a[st]==a[en]:
                ma+=1
            else:
                break
            st-=1
            en+=1
        
        # required length of prefix/suffix for a.
        ra = (n//2)-ma
        
        # maximum size palindrome centered around center of string b
        mb = 0
        st = (n//2)-1
        if n%2==0:
            en = st+1
        else:
            en = st+2
        while st>=0:
            if b[st]==b[en]:
                mb+=1
            else:
                break
            st-=1
            en+=1
        
        # required length of prefix/suffix for b.
        rb = (n//2)-mb
        
        # max length match for prefix of a and suffix of b
        cnt = 0
        for i in range(n):
            if a[i]==b[-i-1]:
                cnt+=1
            else:
                break
        
        # max length match for prefix of b and suffix of a
        count = 0
        for i in range(n):
            if b[i]==a[-i-1]:
                count+=1
            else:
                break
        
        if cnt>=rb or count>=ra or cnt>=ra or count>=rb:
            return True
        return False
