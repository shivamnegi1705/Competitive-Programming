# Question Link:- https://leetcode.com/problems/bulb-switcher-iv/
class Solution:
    def minFlips(self, target: str) -> int:
        #  ans will hold minimum number of flips required to form target
        ans = 0
        
        # bits_set--> will tell us the status of bits from i to n
        bits_set = 0
        
        # n--> length of target string.
        n = len(target)
        
        # traverse string from L to R
        for i in range(n):
            
            # converting current bit to int
            cur = int(target[i])
            
            # (cur=1 and bits_set=0) or (cur=0 and bits_set=1)
            # so we need to flip bits from i index to end.
            if cur!=bits_set:
                # 1 move used
                ans+=1
                # toggling bits from i to end
                bits_set^=1
        return ans
