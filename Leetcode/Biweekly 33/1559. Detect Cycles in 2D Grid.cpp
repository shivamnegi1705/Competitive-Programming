// Question Link:- https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution {
public:
    const int dx[4] = { -1, 0, 1, 0 }; 
    const int dy[4] = { 0, 1, 0, -1 }; 
    int n,m;
    
    bool valid(int x, int y,int n,int m){ 
        if (x < n && x >= 0 && y < m && y >= 0) 
            return 1; 
        else
            return 0; 
    }
    
    bool func(int x, int y, vector<vector<char>>& arr,vector<vector<int>> &vis,int parx, int pary){ 
        vis[x][y] = 1;
        for (int k = 0; k < 4; k++){
            int nx = x + dx[k]; 
            int ny = y + dy[k]; 
            
            if (valid(nx, ny,n,m) == 1 && arr[nx][ny] == arr[x][y] && !(parx == nx and pary == ny)){ 
                if (vis[nx][ny] == 1){
                    return true; 
                } 
                else { 
                bool ans = func(nx, ny, arr, vis, x, y); 
                if (ans == 1) 
                    return true; 
                } 
            } 
        } 
        return false; 
    } 
    bool containsCycle(vector<vector<char>>& grid){
        n = grid.size();
        m = grid[0].size();
        vector<vector<int>> vis;
        for (int i = 0; i < n; i++){
            vector<int> temp;
            for (int j = 0; j < m; j++){ 
                temp.push_back(0);
            }
            vis.push_back(temp);
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            if(ans==1){
                return true;
            }
            for(int j=0;j<m;j++){
                if(vis[i][j]==0){
                    ans = func(i,j,grid,vis,-1,-1);
                }
                if(ans==1){
                    break;
                }
            }
        }
        return false;
        
    }
};
