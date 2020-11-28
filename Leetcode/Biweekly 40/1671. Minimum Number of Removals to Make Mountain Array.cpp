// Question Link:- https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

int dp[1005][1005][2];
class Solution {
public:
    int n;
    int func(int i,int prev,int f,vector<int>& nums){
        if(i==n){
            if(f==1)
                return 0;
            return -10000000;
        }
        if(dp[i][prev][f]!=-1){
            return dp[i][prev][f];
        }
        int ans = 0;
        if(prev==1002){
            int ch1 = 1+func(i+1,i,f,nums);
            int ch2 = func(i+1,prev,f,nums);
            ans = max(ans,max(ch1,ch2));
        }
        else{
            if(f==0){
                if(nums[i]>nums[prev]){
                    ans = max(ans,1+func(i+1,i,f,nums));
                    ans = max(ans,1+func(i+1,i,f^1,nums));
                }
                ans = max(ans,func(i+1,prev,f,nums));
            }
            else{
                if(nums[i]<nums[prev]){
                    ans = max(ans,1+func(i+1,i,f,nums));
                }
                ans = max(ans,func(i+1,prev,f,nums));
            }
        }
        return dp[i][prev][f] = ans;
    }
    int minimumMountainRemovals(vector<int>& nums) {
        n = nums.size();
        memset(dp,-1,sizeof(dp));
        return n-func(0,1002,0,nums);
    }
};
