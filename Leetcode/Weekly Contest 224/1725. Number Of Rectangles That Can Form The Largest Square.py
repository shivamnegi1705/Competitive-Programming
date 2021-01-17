# Question Link:- https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []
        for i in rectangles:
            arr.append(min(i))
        return arr.count(max(arr))
