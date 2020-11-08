# Question Link:- https://leetcode.com/problems/get-maximum-in-generated-array/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0 or n==1:
            return n
        arr = [0 for i in range(n+1)]
        arr[1] = 1
        for i in range(2,n+1):
            if i%2==0:
                arr[i] = arr[i//2]
            else:
                x = (i-1)//2
                arr[i] = arr[x]+arr[x+1]
        return max(arr)
