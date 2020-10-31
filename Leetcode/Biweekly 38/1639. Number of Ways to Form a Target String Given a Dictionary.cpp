// Question Link:- https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

#define ll long long int
class Solution {
public:
    ll mat[26][1005];
    ll n;
    ll m;
    ll mod = 1000000007;
    ll dp[1005][1005];
    string s;
    
    ll func(int i,int j){
        if(i==n){
            return 1;
        }
        if(j==1005){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        ll cnt = 0;
        cnt = (cnt+(func(i+1,j+1)*mat[s[i]-'a'][j])%mod)%mod;
        cnt = (cnt+func(i,j+1))%mod;
        
        return dp[i][j] = cnt;
    }
    
    int numWays(vector<string>& words, string target) {
        s = target;
        n = target.size();
        m = words[0].size();
        memset(mat,0,sizeof(mat));
        for(auto i:words){
            for(int j=0;j<i.size();j++){
                mat[i[j]-'a'][j]+=1;
            }
        }
        memset(dp, -1, sizeof(dp));
        return func(0,0);
        
    }
};
