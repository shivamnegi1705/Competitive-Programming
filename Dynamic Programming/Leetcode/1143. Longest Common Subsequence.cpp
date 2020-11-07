// Question Link:- https://leetcode.com/problems/longest-common-subsequence/

class Solution {
public:
    // n--> size of text1
    // m--> size of text2
    int n,m;
    // dp[index in text 1][index in text 2]
    int dp[1005][1005];
    
    int func(int i,int j,string &s,string &t){
        // when either of a pointer reaches end of the string
        if(i==n || j==m){
            return 0;
        }
        // if the condition is precalculated.
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int ans = 0;
        // if character s[i] and t[j] matches move i-->i+1 and j-->j+1.
        if(s[i]==t[j]){
            ans = 1+func(i+1,j+1,s,t);
        }
        // if character does not match then there are 3 conditions
        // case1:- i-->i+1 , j-->j
        // case2:- i-->i , j-->j+1
        // case3:- i-->i+1 , j-->j+1
        else{
            ans = max(func(i+1,j,s,t),max(func(i,j+1,s,t),func(i+1,j+1,s,t)));
        }
        return dp[i][j] = ans;
    }
    int longestCommonSubsequence(string text1, string text2) {
        n = text1.size();
        m = text2.size();
        // set initial dp to -1
        memset(dp,-1,sizeof(dp));
        return func(0,0,text1,text2);
    }
};
