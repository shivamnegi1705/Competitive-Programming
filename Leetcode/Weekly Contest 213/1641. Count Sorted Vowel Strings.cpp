// Question Link:- https://leetcode.com/problems/count-sorted-vowel-strings/

#define ll long long int
class Solution {
public:
    ll dp[55][5];
    ll func(ll i,ll j,int &n){
        if(i==n){
            return 1;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        ll ans = 0;
        for(ll k=0;k<5;k++){
            if(k>=j){
                ans+=func(i+1,k,n);
            }
        }
        return dp[i][j] = ans;
    }
    int countVowelStrings(int n) {
        memset(dp,-1,sizeof(dp));
        ll ans = 0;
        for(ll i=0;i<5;i++){
            ans+=func(1,i,n);
        }
        return ans;
    }
};
