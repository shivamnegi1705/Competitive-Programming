// Question Link:- https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
public:
    // r--> reversed string of given string.
    string r;
    // n--> size of given string.
    int n;
    // dp[i--> index in s string][j--> index in r string]
    int dp[1005][1005];
    
    int func(int i,int j,string &s){
        // if any pointer reaches end.
        if(i==n || j==n){
            return 0;
        }
        
        // if state is already calculated.
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int ans = 0;
        
        // if character s[i] and r[j] matches move i-->i+1 and j-->j+1.
        if(s[i]==r[j]){
            ans = 1+func(i+1,j+1,s);
        }
        // if character does not match then there are 3 conditions
        // case1:- i-->i+1 , j-->j
        // case2:- i-->i , j-->j+1
        // case3:- i-->i+1 , j-->j+1
        else{
            ans = max(ans,max(func(i+1,j+1,s),max(func(i+1,j,s),func(i,j+1,s))));
        }
        return dp[i][j] = ans;
    }
    int longestPalindromeSubseq(string s) {
        r = s;
        reverse(r.begin(),r.end());
        // set initial dp of -1.
        memset(dp,-1,sizeof(dp));
        n = s.size();
        return func(0,0,s);
    }
};
