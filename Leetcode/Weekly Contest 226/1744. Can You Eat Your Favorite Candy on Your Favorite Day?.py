# Question Link:- https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre = []
        for i in candiesCount:
            if pre==[]:
                pre.append(i)
            else:
                pre.append(pre[-1]+i)
        ans = []
        for i in queries:
            t,day,cap = i
            # print(pre[t],pre[t-1],day)
            if t==0:
                if pre[t]>day:
                    ans.append(True)
                else:
                    ans.append(False)
            else:
                if pre[t]>day:
                    if pre[t-1]//cap<=day:
                        ans.append(True)
                    else:
                        ans.append(False)
                else:
                    ans.append(False)
        return ans
