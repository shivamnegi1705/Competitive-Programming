# Question Link:- https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        
        # if string of size 1 is '?'
        if s=='?':
            return 'a'
        
        # convert string into list of characters
        arr = list(s)
        
        # length of string
        n = len(s)
        
        # all lowercase characters.
        a = 'abcdefghijklmnopqrstuvwxyz'
        
        # traverse string from L to R.
        for i in range(n):
            if arr[i]=='?':
                # check which character we can select.
                for j in a:
                    if i+1<n and i-1>=0:
                        if arr[i+1]!=j and arr[i-1]!=j:
                            arr[i] = j
                            break
                    else:
                        if i+1<n:
                            if arr[i+1]!=j:
                                arr[i] = j
                                break
                        else:
                            if i-1>=0:
                                if arr[i-1]!=j:
                                    arr[i] = j
                                    break
        # return final string
        ans= ''
        for i in arr:
            ans+=i
        return ans
                
                
