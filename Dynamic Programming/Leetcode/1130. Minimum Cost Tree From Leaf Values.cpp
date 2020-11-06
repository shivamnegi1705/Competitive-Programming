// Question Link:- https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution {
public:
    // n--> number of nodes
    int n;
    
    // lookup[i][j] has max value from index i to j
    int lookup[50][50];
    
    // dp[left index][right index]
    int dp[50][50];
    
    int func(int l, int r,vector<int> &arr){
        // if there is one node.
        if(r-l==0){
            return 0;
        }
        
        // if there are 2 nodes pair them up.
        if(r-l==1){
            return arr[l]*arr[r];
        }
        
        // if dp is set then return value.
        if(dp[l][r]!=-1){
            return dp[l][r];
        }
        
        int ans = INT_MAX;
        for(int i=l;i<r;i++){
            // i--> partition from [l to i] and [i+1 to r]
            int cur = (lookup[l][i]*lookup[i+1][r])+func(l,i,arr)+func(i+1,r,arr);
            // take minimum.
            ans = min(ans,cur);
        }
        // set dp with minimum value.
        return dp[l][r] = ans;
    }
    
    int mctFromLeafValues(vector<int>& arr) {
        n = arr.size();
        
        // set dp with -1
        memset(dp,-1,sizeof(dp));
        
        // make lookup table
        for(int i=0;i<n;i++){
            int mex = arr[i];
            for(int j=i;j<n;j++){
                mex = max(mex,arr[j]);
                lookup[i][j] = mex;
            }
        }
        
        return func(0,n-1,arr);
        
    }
};
