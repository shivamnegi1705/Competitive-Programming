// Question Link:- https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution {
public:
    // arr --> (x,y) coordinate of alphabets.
    vector<pair<int,int>> arr;
    // n--> size of string.
    int n;
    // dp[index][finger 1][finger 2]
    int dp[305][26][26];
    int func(int ind, int f1,int f2,string &word){
        // reached end of string.
        if(ind==n){
            return 0;
        }
        // if the value is precalculated.
        if(dp[ind][f1][f2]!=-1){
            return dp[ind][f1][f2];
        }
        
        int cur = word[ind]-'A';
        int val1 = abs(arr[cur].first-arr[f1].first) + abs(arr[cur].second-arr[f1].second);
        int val2 = abs(arr[cur].first-arr[f2].first) + abs(arr[cur].second-arr[f2].second);
        // choice 1 --> use finger 1
        int ch1 = val1+func(ind+1,cur,f2,word);
        // choice 2 --> use finger 2
        int ch2 = val2+func(ind+1,f1,cur,word);
        
        // take minimum of both choices.
        return dp[ind][f1][f2] = min(ch1,ch2);
    }
    
    int minimumDistance(string word){
        n = word.size();
        // initial dp set to -1.
        memset(dp,-1,sizeof(dp));
        // calculate coordinates of alphabets.
        for(int i=0;i<26;i++){
            arr.push_back({i/6,i%6});
        }
        // Take all combinations of both fingers on 26 characters except where both are same.
        int ans = INT_MAX;
        for(int i=0;i<26;i++){
            for(int j=0;j<26;j++){
                if(i!=j){
                    // take minimum ans
                    ans = min(ans,func(0,i,j,word));
                }
            }
        }
        return ans;
    }
};
