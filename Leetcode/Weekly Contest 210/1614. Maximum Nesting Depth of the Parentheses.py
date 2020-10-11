# Question Link:- https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        
        # stack to push ( 
        st = []
        
        # number of ( in stack
        n = 0
        
        # ans --> to store max depth
        ans = 0
        
        # Traverse in string from L to R
        for i in s:
            # Push (
            if i=='(':
                st.append('(')
                n+=1
                ans = max(ans,n)
            # Pop )
            elif i==')':
                st.pop()
                n-=1
                # Update ans
                ans = max(ans,n)
        return ans
