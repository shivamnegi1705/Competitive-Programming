// Question Link:- https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution {
public:
    // dp[index][vowels]
    int dp[55][5];
    
    // ind--> index from 0 to n-1
    // cur--> 0 to 4 representing 'a','e','i','o','u'
    int helper(int ind,int cur,int &n){
        if(ind==n){
            return 1;
        }
        // if dp is set then return value.
        if(dp[ind][cur]!=-1){
            return dp[ind][cur];
        }
        int ans = 0;
        // Taking vowel greater than or equal to current vowel.
        for(int i=0;i<5;i++){
            if(i>=cur){
                ans+=helper(ind+1,i,n);
            }
        }
        return dp[ind][cur] = ans;
    }
    
    int countVowelStrings(int n) {
        int ans = 0;
        // setting dp with -1
        memset(dp,-1,sizeof(dp));
        
        // can start string with any vowel(a,e,i,o,u)
        for(int i=0;i<5;i++){
            ans+=helper(1,i,n);
        }
        return ans;
    }
};
