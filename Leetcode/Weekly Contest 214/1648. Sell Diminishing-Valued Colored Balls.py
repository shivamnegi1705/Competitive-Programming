# Question Link:- https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def func(n):
            x = (n*(n+1))
            return x//2
        arr = []
        mod = pow(10,9)+7
        for i in inventory:
            arr.append(i)
        arr.sort(reverse=True)
        n = len(inventory)
        cnt = 1
        ans = 0
        for i in range(n-1):
            diff = (arr[i]-arr[i+1])*cnt
            d = arr[i]-arr[i+1]
            if orders>=diff:
                val1 = func(arr[i])
                val2 = func(arr[i+1])
                val = val1-val2
                val = (val*cnt)%mod
                ans = (ans+val)%mod
                cnt+=1
                orders-=diff
                if orders==0:
                    break
            else:
                diff = orders
                m = diff%(cnt)
                x = diff//(cnt)
                orders = 0
                val1 = func(arr[i])
                val2 = func(arr[i]-x)
                val = val1-val2
                val = (val*cnt)%mod
                ans = (ans+val)%mod
                ans = (ans+((arr[i]-x)*m)%mod)%mod
                cnt+=1
                break
        if orders!=0:
            t = orders//cnt
            m = orders%cnt
            val1 = func(arr[-1])
            val2 = func(arr[-1]-t)
            val = val1-val2
            val = (val*cnt)%mod
            ans = (ans+val)%mod
            ans = (ans+((arr[-1]-t)*m)%mod)%mod
        return ans
                
