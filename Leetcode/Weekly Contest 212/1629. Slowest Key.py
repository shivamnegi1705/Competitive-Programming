# Question Link:- https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, arr: List[int], key: str) -> str:
        ans = [0 for i in range(26)]
        arr = [0]+arr
        for i in range(1,len(arr)):
            cur = ord(key[i-1])-ord('a')
            ans[cur] = max(ans[cur],arr[i]-arr[i-1])
        cnt = -1
        ch = ''
        for i in range(26):
            if cnt<ans[i]:
                cnt = ans[i]
                ch = i
            elif cnt==ans[i]:
                ch = i
        return chr(97+ch)
