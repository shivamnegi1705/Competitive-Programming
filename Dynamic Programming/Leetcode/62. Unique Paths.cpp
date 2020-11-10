// Question Link:- https://leetcode.com/problems/unique-paths/

class Solution {
public:
    // dp[current row][current column]
    int dp[105][105];
    int func(int i,int j,int &n,int &m){
        // if we reach end point.
        if(i==m-1 && j==n-1){
            return 1;
        }
        // if we are out of bounds
        if(i>=m || i<0 || j>=n || j<0){
            return 0;
        }
        // if the state is already precalculated.
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        // 2choices--> either move down or move right.
        return dp[i][j] = func(i+1,j,n,m)+func(i,j+1,n,m);
    }
    int uniquePaths(int m, int n) {
        // set dp to -1
        memset(dp,-1,sizeof(dp));
        return func(0,0,n,m);
    }
};
