# Question Link:- https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        n = len(ages)
        for i in range(len(scores)):
            arr.append([ages[i],scores[i]])
        arr.sort()
        ans = [arr[i][1] for i in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                if arr[i][1]>=arr[j][1]:
                    ans[i] = max(ans[i],ans[j]+arr[i][1])
        return max(ans)
