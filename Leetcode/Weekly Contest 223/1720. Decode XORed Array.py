# Question Link:- https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            x = i^first
            ans.append(x)
            first = x
        return ans
            
        
