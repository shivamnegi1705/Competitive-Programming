// Question Link:- https://leetcode.com/problems/minimum-path-sum/

class Solution {
public:
    // r--> number of rows
    // c--> number of cols
    int r,c;
    // inf--> large value
    const int inf = 10000000;
    // dp[current row][current col]
    int dp[205][205];
    
    int func(int i,int j,vector<vector<int>>& grid){
        // bottom left corner
        if(i==r-1 && j==c-1){
            return grid[i][j];
        }
        // out of bounds
        if(i<0 || j<0 || i>=r || j>=c){
            return inf;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        // move left.
        int ch1 = grid[i][j]+func(i,j+1,grid);
        // move right.
        int ch2 = grid[i][j]+func(i+1,j,grid);
        // take minimum of both choices
        return dp[i][j] = min(ch1,ch2);
        
    }
    int minPathSum(vector<vector<int>>& grid) {
        r = grid.size();
        c = grid[0].size();
        memset(dp,-1,sizeof(dp));
        return func(0,0,grid);
    }
};
