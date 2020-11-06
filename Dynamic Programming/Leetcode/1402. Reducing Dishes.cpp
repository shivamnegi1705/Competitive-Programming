// Question Link:- https://leetcode.com/problems/reducing-dishes/

class Solution {
public:
    // n--> size of satisfaction array.
    int n;
    // dp[index][time];
    int dp[505][505];
    
    int func(int ind,int time,vector<int>&arr){
        if(ind==n){
            return 0;
        }
        // if dp is set for the parameters then return value of dp.
        if(dp[ind][time]!=-1){
            return dp[ind][time];
        }
        // choice1 --> include current dish.
        int ch1 = time*arr[ind]+func(ind+1,time+1,arr);
        
        // choice2 --> don't include current dish.
        int ch2 = func(ind+1,time,arr);
        
        // return max of choice 1 and 2.
        return dp[ind][time] = max(ch1,ch2);
    }
    int maxSatisfaction(vector<int>& satisfaction) {
        n = satisfaction.size();
        
        // set dp to -1.
        memset(dp,-1,sizeof(dp));
        
        // sort dishes in ascending order so that max satisfaction dish give more output.
        sort(satisfaction.begin(),satisfaction.end());
        
        return func(0,1,satisfaction);
    }
};
