# Question Link:- https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mapper = {}
        p = [2**i for i in range(22)]
        for i in deliciousness:
            if i in mapper:
                mapper[i]+=1
            else:
                mapper[i] = 1
        ans = 0
        mod = 10**9+7
        for i in mapper:
            cur = i
            g = mapper[cur]
            for j in p:
                rem = j-cur
                if rem<i:
                    continue
                if rem in mapper:
                    if rem==cur and g>1:
                        ans = (ans+(g*(g-1))//2)%mod
                    if rem!=cur:
                        k = mapper[rem]
                        ans = (ans+(g*k)%mod)%mod
        return ans
