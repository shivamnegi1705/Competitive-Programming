# Question Link:- https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, arr: List[int]) -> bool:
        n = len(arr)
        temp = arr[::]
        temp.sort()
        for i in range(n):
            if arr[:i]+arr[i:]==temp or arr[i::]+arr[:i:]==temp:
                return True
        return False
