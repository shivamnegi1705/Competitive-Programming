# Question Link:- https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        b = b%n
        
        def func(q,ans,temp):
            t = [i for i in q]
            temp = []
            while True:
                for i in range(n):
                    if i%2!=0:
                        t[i] = str((int(t[i])+a)%10)
                x = ''
                for i in t:
                    x+=i
                if x in ans:
                    break
                ans[x] = 1
                temp.append(x)
            return [ans,temp]
        
        ans = {}
        func(s,ans,[])
        
        arr = []
        for i in ans:
            arr.append(i)
            
        while True:
            if arr==[]:
                break
            temp = []
            for i in arr:
                cur = i 
                while True:
                    cur = cur[n-b:n]+cur[0:n-b]
                    if cur!=i:
                        if cur not in ans:
                            ans,temp = func(cur,ans,temp)
                    else:
                        break
            arr=temp[::]
        arr = []
        for i in ans:
            arr.append(i)
        arr.sort()
        return arr[0]
        
