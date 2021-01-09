# Question Link:- https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        cnt = 1
        ans = 0
        cur = cnt
        for i in range(n):
            # print(cur)
            if i%7==0 and i!=0:
                cnt+=1
                cur = cnt
            ans+=cur
            cur+=1
            
        return ans
