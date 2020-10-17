// Question Link:- https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

# define ll long long int
class Solution {
public:
    ll mod = 1000000007;
    ll dp[1004][1004][2];
    ll n;
    ll func(ll pos,ll s,ll st){
        if(pos==n){
            return (!st && !s);
        }
        
        if(dp[pos][s][st]!=-1){
            return dp[pos][s][st];
        }
        
        ll score = 0;
        if(st){
            score = (score+func(pos+1,s,1))%mod;
            score = (score+func(pos+1,s,0))%mod;
            if(s>0){
                score = (score+func(pos+1,s-1,1))%mod;
            }
        }
        else{
            if(s>0){
                score = (score+func(pos+1,s-1,1))%mod;
            }
            score = (score+func(pos+1,s,0))%mod;
        }
        return dp[pos][s][st] = score;
    }
    
    int numberOfSets(int p, int k) {
        n = p;
        memset(dp, -1, sizeof dp);
        int ans = func(0, k, 0);
        return ans;
    }
};
