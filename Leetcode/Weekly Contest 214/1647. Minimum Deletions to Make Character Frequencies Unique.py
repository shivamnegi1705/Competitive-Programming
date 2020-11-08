# Question Link:- https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0 for i in range(26)]
        for i in s:
            x = ord(i)-97
            freq[x]+=1
        arr = []
        for i in freq:
            if i!=0:
                arr.append(i)
        arr.sort()
        d = {}
        ans = 0
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                f = i
                while f>0:
                    if f in d:
                        f-=1
                    else:
                        break
                if f!=0:
                    d[f] = 1
                ans+=(i-f)
        return ans
