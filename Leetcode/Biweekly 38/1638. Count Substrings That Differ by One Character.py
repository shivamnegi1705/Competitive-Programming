# Question Link:- https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                pt1,pt2 = i,j
                f = 0
                cnt = 0
                while pt1<n and pt2<m:
                    if s[pt1]==t[pt2]:
                        if f==1:
                            cnt+=1
                        else:
                            pass
                    else:
                        if f==0:
                            f = 1
                            cnt+=1
                        else:
                            break
                    pt1+=1
                    pt2+=1
                ans+=cnt
        return ans
