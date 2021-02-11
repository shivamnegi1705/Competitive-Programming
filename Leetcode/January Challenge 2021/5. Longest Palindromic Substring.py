# Question Link:- https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = []
        for i in s:
            arr.append('#')
            arr.append(i)
        arr.append('#')
        n = len(arr)
        mex = [0 for i in range(n)]
        l = 0
        r = -1
        for i in range(n):
            if i>r:
                k = 0
            else:
                j = r-i+l
                k = min(mex[j],r-i)
            while i-k>=0 and i+k<n and arr[i-k]==arr[i+k]:
                k+=1
            k-=1
            mex[i] = k
            if i+k>r:
                l = i-k
                r = i+k
        m = max(mex)
        ind = mex.index(m)
        ans = ''
        if arr[ind]!='#':
            ans+=arr[ind]
        i = ind-1
        j = ind+1
        while i>=0 and j<n and arr[i]==arr[j]:
            if arr[i]!='#':
                ans = arr[i]+ans+arr[j]
            i-=1
            j+=1
        return ans
