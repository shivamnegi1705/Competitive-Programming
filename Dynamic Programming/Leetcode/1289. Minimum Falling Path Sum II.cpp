// Question Link:- https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
public:
    // r--> number of rows, c--> number of columns
    int r,c;
    // dp[row][column]
    int dp[205][205];
    // negative inf.
    const int ninf = -30000;
    
    int func(int i,int j,vector<vector<int>> &arr){
        // last row
        if(i==r-1){
            return 0;
        }
        // if substask is already calculated.
        if(dp[i][j]!=ninf){
            return dp[i][j];
        }
        int ans = 10000000;
        for(int k=0;k<c;k++){
            if(j!=k)
                ans = min(ans,arr[i+1][k]+func(i+1,k,arr));
        }
        // set dp with minimum value.
        return dp[i][j] = ans;
    }
    int minFallingPathSum(vector<vector<int>>& arr) {
        r = arr.size();
        c = arr[0].size();
        int ans = 10000000;
        // set initial dp to negative inf.
        for(int i=0;i<205;i++){
            for(int j=0;j<205;j++){
                dp[i][j] = ninf;
            }
        }
        // find minimum ans for each starting point in the first row and take their minimum.
        for(int i=0;i<c;i++){
            ans = min(ans,arr[0][i]+func(0,i,arr));
        }
        return ans;
        
    }
};
