// Question Link:- https://leetcode.com/problems/climbing-stairs/

class Solution {
public:
    int dp[50];
    int func(int i,int &n){
        if(i==n){
            return 1;
        }
        if(i>n){
            return 0;
        }
        if(dp[i]!=-1){
            return dp[i];
        }
        return dp[i] = func(i+1,n)+func(i+2,n);
    }
    int climbStairs(int n) {
        memset(dp,-1,sizeof(dp));
        return func(0,n);
    }
};
