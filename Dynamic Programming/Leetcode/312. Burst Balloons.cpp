// Question Link:- https://leetcode.com/problems/burst-balloons/

class Solution {
public:
    // n--> size of given array.
    int n;
    // dp[start][end]
    int dp[505][505];
    int func(int l,int r,vector<int>& nums){
        // no balloon
        if(l>r){
            return 0;
        }
        // state already calculated.
        if(dp[l][r]!=-1){
            return dp[l][r];
        }
        // only one balloon.
        if(l==r){
            return dp[l][r] = nums[l-1]*nums[l]*nums[l+1];
        }
        
        int ans = 0;
        // make all available partitions.
        for(int i=l;i<=r;i++){
            int cost = nums[l-1]*nums[r+1]*nums[i];
            ans = max(ans,cost+func(l,i-1,nums)+func(i+1,r,nums));
        }
        return dp[l][r] = ans;
    }
    int maxCoins(vector<int>& arr) {
        // initial dp to -1
        memset(dp,-1,sizeof(dp));
        // adding 1 at the start and end
        vector<int> nums ={1};
        for(auto i:arr){
            if(i)
                nums.push_back(i);
        }
        nums.push_back(1);
        n = nums.size()-2;
        return func(1,n,nums);
    }
};
