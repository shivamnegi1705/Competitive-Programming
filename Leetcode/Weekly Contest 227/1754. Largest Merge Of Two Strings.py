# Question Link:- https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ind1,ind2 = 0,0
        n,m = len(word1),len(word2)
        ans = ''
        while ind1<n and ind2<m:
            if word1[ind1]==word2[ind2]:
                f = -1
                x = ind1
                y = ind2
                while x<n and y<m:
                    if word1[x]==word2[y]:
                        x+=1
                        y+=1
                    else:
                        f = 1
                        break
                if f==-1:
                    if y==m:
                        ans+=word1[ind1]
                        ind1+=1
                    else:
                        ans+=word2[ind2]
                        ind2+=1
                else:
                    if word1[x]>word2[y]:
                        ans+=word1[ind1]
                        ind1+=1
                    else:
                        ans+=word2[ind2]
                        ind2+=1
            else:
                if word1[ind1]>word2[ind2]:
                    ans+=word1[ind1]
                    ind1+=1
                else:
                    ans+=word2[ind2]
                    ind2+=1
        while ind1<n:
            ans+=word1[ind1]
            ind1+=1
        while ind2<m:
            ans+=word2[ind2]
            ind2+=1
        return ans
