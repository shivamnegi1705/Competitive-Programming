# Question Link:- https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, s: str) -> str:
        ans = []
        i = 0
        while i<len(s):
            if s[i]=='G':
                ans.append('G')
                i+=1
            elif s[i]=='(' and s[i+1]==')':
                ans.append('o')
                i+=2
            else:
                ans.append('al')
                i+=4
        t = ''
        for i in ans:
            t+=i
        return t
