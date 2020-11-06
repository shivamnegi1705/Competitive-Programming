// Question Link:- https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
public:
    // change in y direction
    int dy[3] = {1,-1,0};
    // r--> number of rows, c--> number of columns
    int r,c;
    // dp[row][column]
    int dp[105][105];
    
    int func(int i,int j,vector<vector<int>> &A){
        // last row
        if(i==r-1){
            return 0;
        }
        // if substask is already calculated.
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int ans = 10000000;
        for(int k=0;k<3;k++){
            int di = i+1;
            int dj = j+dy[k];
            // find valid next point and take minimum.
            if(di>=0 && di<r && dj>=0 && dj<c){
                ans = min(ans,A[di][dj]+func(di,dj,A));
            }
        }
        // set dp with minimum value.
        return dp[i][j] = ans;
        
    }
    int minFallingPathSum(vector<vector<int>>& A) {
        r = A.size();
        c = A[0].size();
        int ans = 10000000;
        // set initial dp to -1
        memset(dp,-1,sizeof(dp));
        // find minimum ans for each starting point in the first row and take their minimum.
        for(int i=0;i<c;i++){
            ans = min(ans,A[0][i]+func(0,i,A));
        }
        return ans;
    }
};
