# Question Link:- https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1,d2 = {},{}
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i] = 1
        for i in word2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i] = 1
        for i in d1:
            if i not in d2:
                return False
        for i in d2:
            if i not in d1:
                return False
        arr,brr = [],[]
        for i in d1:
            arr.append(d1[i])
        for i in d2:
            brr.append(d2[i])
        arr.sort()
        brr.sort()
        if len(brr)!=len(arr):
            return False
        for i in range(len(arr)):
            if arr[i]!=brr[i]:
                return False
        return True
