# Question Link:- https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        pre = [0 for i in range(n)]
        suf = [0 for i in range(n)]
        
        pre[0] = 1
        for i in range(1,n):
            if arr[i]>=arr[i-1] and pre[i-1]==1:
                pre[i] = 1
        
        suf[n-1] = 1
        for i in range(n-2,-1,-1):
            if arr[i]<=arr[i+1] and suf[i+1]==1:
                suf[i] = 1
        
        if pre[n-1]==1:
            return 0
        
        lo = 1
        hi = n
        ans = n
        while lo<=hi:
            mid = (lo+hi)//2
            f = False
            for i in range(mid-1,n):
                if i-mid>=0:
                    l = pre[i-mid]
                else:
                    l = True
                if i+1<n:
                    r = suf[i+1]
                else:
                    r = True
                k = True
                if i-mid>=0 and i+1<n:
                    if arr[i-mid]<=arr[i+1]:
                        k = True
                    else:
                        k = False
                f = f|(l&r&k)
            if f==True:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
        
