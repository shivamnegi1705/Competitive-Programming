#Question Link:- https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, s: str) -> str:
        arr = []
        for i in s:
            if i in '0123456789':
                arr.append(i)
        n = len(arr)
        ans = ''
        i = 0
        while i<n:
            rem = n-i
            if rem>4 or rem==3:
                ans+=arr[i]+arr[i+1]+arr[i+2]
                i+=3
                ans+='-'
            else:
                ans+=arr[i]+arr[i+1]
                i+=2
                ans+='-'
        return ans[:len(ans)-1]
