# Question Link:- https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        ind = 0
        for i in pieces:
            for j in i:
                d[j] = ind
            ind+=1
        i = 0
        while i<len(arr):
            x = arr[i]
            if x in d:
                temp = pieces[d[x]]
                for j in range(len(temp)):
                    if arr[i]==temp[j]:
                        pass
                    else:
                        return False
                    i+=1
            else:
                return False
        return True
