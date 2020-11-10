// Question Link:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
public:
    // n--> size of prices length
    int n;
    // dp[index][type-->sell or buy]
    int dp[50005][2];
    int func(int ind,int type,int &fee,vector<int> &prices){
        // reached end
        if(ind==n){
            return 0;
        }
        // if state is already precalculated.
        if(dp[ind][type]!=-1){
            return dp[ind][type];
        }
        int ans = 0;
        // we can buy a stock.
        if(type==0){
            // we can either buy a stock now or buy it later
            ans = max(ans,func(ind+1,1,fee,prices)-fee-prices[ind]);
            ans = max(ans,func(ind+1,0,fee,prices));
        }
        else{
            // we can either sell a stock now or sell it later
            ans = max(ans,func(ind+1,0,fee,prices)+prices[ind]);
            ans = max(ans,func(ind+1,1,fee,prices));
        }
        
        return dp[ind][type] = ans;
    }
    int maxProfit(vector<int>& prices, int fee) {
        n = prices.size();
        memset(dp,-1,sizeof(dp));
        return func(0,0,fee,prices);
    }
};
