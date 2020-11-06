// Question Link:- https://leetcode.com/problems/cherry-pickup-ii/

class Solution {
public:
    // r--> number of rows
    // c--> number of columns
    int r,c;
    // coor[] --> change in y direction.
    int coor[3] = {1,-1,0};
    
    // dp[x-coord][y-coord for 1st robot][y-coord for 2nd robot]
    int dp[71][71][71];
    
    int func(int x,int y1,int y2,vector<vector<int>>& grid){
        // last row.
        if(x==r-1){
            return 0;
        }
        // if dp is set then return pre-calculated value.
        if(dp[x][y1][y2]!=-1){
            return dp[x][y1][y2];
        }
        
        int ans = 0;
        for(int i=0;i<3;i++){
            int dx = x+1;
            int dy1 = y1+coor[i];
            if(dy1>=0 && dy1<c){
                for(int j=0;j<3;j++){
                    int dy2 = y2+coor[j];
                    if(dy2>=0 && dy2<c){
                        // both robots on same coordinates
                        if(dy1==dy2){
                            ans = max(ans,grid[dx][dy1]+func(dx,dy1,dy2,grid));
                        }
                        // robots on different coordinates.
                        else{
                            ans = max(ans,grid[dx][dy1]+grid[dx][dy2]+func(dx,dy1,dy2,grid));
                        }
                    }
                }
            }
        }
        // set dp with max value.
        return dp[x][y1][y2] = ans;
        
    }
    int cherryPickup(vector<vector<int>>& grid) {
        r = grid.size();
        c = grid[0].size();
        // intial dp with -1.
        memset(dp,-1,sizeof(dp));

        return func(0,0,c-1,grid)+grid[0][0]+grid[0][c-1];
    }
};
