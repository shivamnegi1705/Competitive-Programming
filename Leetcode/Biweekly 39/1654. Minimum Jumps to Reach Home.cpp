// Question Link:- https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution {
public:
    map<int,int> mapper;
    int dp[4005][2];
    const int inf = 10000000;
    int func(int i,int &a,int &b,int &x,int t){
        if(i>4000){
            return inf;
        }
        if(i==x){
            return 0;
        }
        if(dp[i][t]!=-1){
            return dp[i][t];
        }
        int ans = inf;
        dp[i][t] = ans;
        if(i-b>=0 && t==0 && mapper[i-b]==0){
            ans = min(ans,1+func(i-b,a,b,x,1));
        }
        if(mapper[i+a]==0)
            ans = min(ans,1+func(i+a,a,b,x,0));
        return dp[i][t] = ans;
    }
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        for(auto i:forbidden){
            mapper[i] = 1;
        }
        memset(dp,-1,sizeof(dp));
        int ans = func(0,a,b,x,0);
        if(ans==inf){
            return -1;
        }
        return ans;
    }
};
