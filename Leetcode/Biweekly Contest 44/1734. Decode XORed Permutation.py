# Question Link:- https://leetcode.com/problems/decode-xored-permutation/

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x = 0
        y = 0
        for i in range(1,len(encoded)+2):
            x = x^i
        for i in range(len(encoded)):
            if i%2==0:
                continue
            y = y^encoded[i]
        f = x^y
        ans = []
        ans.append(f)
        for i in encoded:
            ans.append(ans[-1]^i)
        return ans
