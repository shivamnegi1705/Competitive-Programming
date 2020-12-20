# Question Link:- https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, arr: List[int], k: int) -> int:
        ans = deque([])
        n = len(arr)
        ans.append([0,arr[0]])
        for i in range(1,n):
            while i-ans[0][0]>k:
                ans.popleft()
            r = [i,arr[i]+ans[0][1]]
            while len(ans)>0 and ans[-1][1]<=r[1]:
                ans.pop()
            ans.append(r)
        return ans[-1][1]
