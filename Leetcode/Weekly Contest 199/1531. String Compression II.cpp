// Question Link:- https://leetcode.com/problems/string-compression-ii/

// dp[current_index][previous_character][remaining_moves_out_of_k][length_of_repeated_character_till_now]
int dp[101][27][101][101];
class Solution {
public:
    
    // size of string.
    int n;
    
    // helper function to calculate length of compressed string. 
    int helper(int v,int p){
        if(p==26){
            return -1;
        }
        if(v==1){
            return 0;
        }
        if(v<=9){
            return 1;
        }
        if(v<=99)
            return 2;
        return 3;
    }
    
    int func(int i,int prev,int rem,int l,string &s){
        // string ends here so add compressed length of last un-calculated part.
        if(i>=n){
            return helper(l,prev)+1;
        }
        
        int &ans = dp[i][prev][rem][l];
        // if dp value is not -1 then it's been calculated.
        if(~ans){
            return ans;
        }
        
        // inclusion and exclusion variable for current character
        int excl = 10000000;
        int incl = 10000000;
        
        int cur = s[i]-'a';
        // if we have some moves remaining then we can delete current character
        if(rem>0)
            excl = func(i+1,prev,rem-1,l,s);
        // if we include this and it's same as previous character.
        if(cur==prev){
            incl = func(i+1,cur,rem,l+1,s);
        }
        // if we include this and it's not same as previous character 
        // then using helper function find compressed part length for current character.
        else{
            incl = helper(l,prev) + 1 + func(i+1,cur,rem,1,s);
        }
        
        return ans = min(incl,excl);
    }
    
    int getLengthOfOptimalCompression(string s, int k) {
        n = s.size();
        // setting dp to -1
        memset(dp,-1,sizeof(dp));
        return func(0,26,k,1,s);
    }
};
