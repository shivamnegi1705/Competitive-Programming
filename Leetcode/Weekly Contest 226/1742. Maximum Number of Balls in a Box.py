# Question Link:- https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def func(x):
            ans = 0
            for i in str(x):
                ans+=int(i)
            return ans
        d = {}
        for i in range(lowLimit,highLimit+1):
            x = func(i)
            if x in d:
                d[x]+=1
            else:
                d[x] = 1
        ans = -1
        val = -1
        for i in d:
            ans = max(ans,d[i])
        return ans
