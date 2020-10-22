# Question Link:- https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
class Solution:
    def thousandSeparator(self, n: int) -> str:
        cnt = 0
        p = str(n)
        ans = ''
        for i in range(-1,-len(p)-1,-1):
            ans = p[i]+ans
            cnt+=1
            if cnt%3==0:
                ans = '.'+ans
                cnt = 0
        if ans[0]=='.':
            ans = ans[1::]
        return ans
