# Question Link:- https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        ans = 0
        for i in d:
            x = k-i
            if x in d:
                if i==x:
                    ans+=(d[i]//2)
                    d[i] = d[i]%2
                else:
                    y = min(d[i],d[x])
                    ans+=y
                    d[i]-=y
                    d[x]-=y
        return ans
                    
