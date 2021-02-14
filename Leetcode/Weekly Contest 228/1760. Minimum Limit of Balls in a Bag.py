# Question Link:- https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        def func(mid):
            cnt = 0
            for i in range(n):
                cnt+=nums[i]//mid
                if nums[i]%mid==0:
                    cnt-=1
            # print(mid,cnt)
            return cnt<=maxOperations
        lo = 1
        hi = 10**10
        while lo<hi:
            mid = (lo+hi)//2
            x = func(mid)
            # print(x,mid)
            if x==True:
                hi = mid
            else:
                lo = mid
            if hi-lo==1:
                break
        if func(lo)==True:
            return lo
        return hi
