# Question Link:- https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # length of given string.
        n = len(s)
        
        # array to hold final ans.
        ans = ['' for i in range(n)]
        
        # loop through string from left to right.
        for i in range(n):
            # position of s[i] character is indices[i]
            cur_index = indices[i]
            # set the indices[i] th index to s[i]
            ans[cur_index] = s[i]
        
        # w--> final string.
        w = ''
        for i in ans:
            w+=i
        return w
        
