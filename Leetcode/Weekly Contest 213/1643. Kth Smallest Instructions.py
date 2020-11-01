# Question Link:- https://leetcode.com/problems/kth-smallest-instructions/

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        fac = [1]
        for i in range(1,31):
            fac.append(fac[-1]*i)
        @lru_cache(None)
        def func(v,h,k):
            if k==1:
                return 'H'*h+'V'*v
            val = fac[v+h-1]
            val = val//fac[v]
            val = val//fac[h-1]
            if k<=val:
                return 'H'+func(v,h-1,k)
            else:
                return 'V'+func(v-1,h,k-val)
        return func(*destination,k)
        
