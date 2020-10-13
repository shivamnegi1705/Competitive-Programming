# Question Link:- https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # length of given string.
        n = len(s)
        
        # cur--> keeps track which character is repeated continuously.
        cur = s[0]
        
        # max cost in repeated characters segment.
        # if there are x characters repeated then we need to delete x-1 characters so we leave character which max cost and delete all other characters.
        mex = cost[0]
        
        # total cost of segment.
        cur_cost = cost[0]
        
        # ans--> final cost.
        ans = 0
        
        # cnt--> number of same elements in a segment.
        cnt = 1
        
        # Traverse string from L to R.
        for i in range(1,n):
            # if current character(s[i]) matches.
            if s[i]==cur:
                # Update total cost of segment.
                cur_cost+=cost[i]
                # Update max cost in a segment.
                mex = max(mex,cost[i])
                # Update count of same characters in a segment.
                cnt+=1
            else:
                # if there are more than 1 characters then add cost of cnt-1 repeated characters.
                if cnt>1:
                    ans+=(cur_cost-mex)
                # Reset values for new segment.
                cur = s[i]
                cur_cost = cost[i]
                cnt = 1
                mex = cost[i]
        
        if cnt>1:
            ans+=(cur_cost-mex)
        # Return final cost.
        return ans
