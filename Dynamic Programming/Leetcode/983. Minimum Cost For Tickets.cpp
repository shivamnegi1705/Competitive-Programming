// Question Link:- https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution {
public:
    // map to check whether we travel on given day or not
    map<int,int> travel;
    // dp[days]
    int dp[400];
    int func(int i,vector<int>& costs){
        // if current day > max day value.
        if(i>365){
            return 0;
        }
        // if state has been calculated.
        if(dp[i]!=0){
            return dp[i];
        }
        
        int ans = INT_MAX;
        // we travel on current day.
        if(travel[i]==1){
            // can take pass of 1 day.
            int ch1 = costs[0]+func(i+1,costs);
            // can take pass of 7 days.
            int ch2 = costs[1]+func(i+7,costs);
            // can take pass of 30 days.
            int ch3 = costs[2]+func(i+30,costs);
            ans = min(ans,min(ch1,min(ch2,ch3)));
        }
        // we donot travel on current day.
        else{
            // no need to take pass.
            ans = func(i+1,costs);
        }
        // set dp
        return dp[i] = ans;
    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        for(auto i:days){
            travel[i] = 1;
        }
        // initial state of dp --> 0
        memset(dp,0,sizeof(dp));
        return func(1,costs);
    }
};
