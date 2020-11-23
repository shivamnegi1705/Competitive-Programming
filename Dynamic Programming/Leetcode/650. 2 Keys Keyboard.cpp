// Question Link:- https://leetcode.com/problems/2-keys-keyboard/

class Solution {
public:
    // dp[current size][current copied size]
    int dp[1005][1005];
    int func(int i,int &n,int cur){
        // if current size is n
        if(i==n){
            return 0;
        }
        // if size is greater than n
        if(i>n){
            return 10000000;
        }
        if(dp[i][cur]!=-1){
            return dp[i][cur];
        }
        int ans = 10000000;
        // copy then paste
        ans = min(ans,2+func(i+i,n,i));
        // only paste
        ans = min(ans,1+func(i+cur,n,cur));
        
        // set dp
        return dp[i][cur] = ans;
    }
    int minSteps(int n) {
        // initial dp to -1
        memset(dp,-1,sizeof(dp));
        if(n==1){
            return 0;
        }
        return 1+func(1,n,1);
    }
};
