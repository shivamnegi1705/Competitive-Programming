# Question Link:- https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if len(nums)==1:
            if nums[0]==x:
                return 1
            else:
                return -1
        if sum(nums)==x:
            return len(nums)
        pre = [nums[0]]
        n = len(nums)
        ans = 10**18
        if pre[0]==x:
            ans = min(ans,1)
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
            if pre[-1]==x:
                ans = min(ans,i+1)
        s = 0
        for i in range(n-1,0,-1):
            s+=nums[i]
            lo = 0
            hi = i-1
            if s==x:
                ans = min(ans,n-i)
            while lo<hi:
                mid = (lo+hi)//2
                if s+pre[mid]<x:
                    lo = mid
                else:
                    hi = mid
                if hi-lo==1:
                    break
            if pre[lo]+s==x:
                ans = min(ans,lo+1+n-i)
            if pre[hi]+s==x:
                ans = min(ans,hi+1+n-i)
        if ans==10**18:
            return -1
        return ans
