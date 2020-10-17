# Question Link:- https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        x = (n*5)//100
        s = 0
        for i in range(x,n-x):
            s+=arr[i]
        return (s/(n-2*x))
        
