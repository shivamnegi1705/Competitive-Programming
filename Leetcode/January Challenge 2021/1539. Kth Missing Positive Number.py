# Question Link:- https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        temp = [0 for i in range(3000)]
        for i in arr:
            temp[i] = 1
        for i in range(3000):
            if temp[i]==0:
                cnt+=1
                if cnt==k+1:
                    return i
