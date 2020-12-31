# Question Link:- https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        arr = []
        ans = 0
        for i in range(n):
            if apples[i]!=0:
                heapq.heappush(arr,[i+days[i]-1,apples[i]])
            if len(arr)>0:
                while len(arr)>0 and arr[0][0]<i:
                    heapq.heappop(arr)
                if len(arr)==0:
                    continue
                l,cnt = heapq.heappop(arr)
                if l>=i:
                    cnt-=1
                    ans+=1
                    if cnt!=0:
                        heapq.heappush(arr,[l,cnt])
        cur = n
        # print(arr,ans)
        while len(arr)!=0:
            while len(arr)>0 and arr[0][0]<cur:
                heapq.heappop(arr)
            if len(arr)==0:
                break
            l,cnt = heapq.heappop(arr)
            if l>=cur:
                cnt-=1
                ans+=1
                if cnt!=0:
                    heapq.heappush(arr,[l,cnt])
                cur+=1
        return ans
