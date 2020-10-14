# Question Link:- https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/submissions/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # we can use difference array for request [x,y] we can add 1 at index x and 
        # subtract 1 from y+1 index this will increase the frequency by 1 for range 
        # x to y.
        
        # After calculating the frequency for each index we can greedily match greater number with 
        # greater frequency.
        
        mex = (10**5)+5
        ans = [0 for i in range(mex)]
        # Processing each request.
        for i in requests:
            x,y = i
            ans[x]+=1
            ans[y+1]-=1
        # Taking prefix sum.
        for i in range(1,mex):
            ans[i] = ans[i]+ans[i-1]
        # Sorting nums in decreasing order.
        nums.sort(reverse=True)
        # Taking non-zero frequency and sort it in decreasing order.
        freq = []
        for i in ans:
            if i!=0:
                freq.append(i)
        freq.sort(reverse=True)
        
        mod = (10**9)+7
        # cnt--> to calculate maximum total sum
        cnt = 0
        for i in range(min(len(freq),len(nums))):
            cnt = (cnt+((freq[i]*nums[i])%mod))%mod
        return cnt
