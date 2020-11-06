// Question Link:- https://leetcode.com/problems/matrix-block-sum/

class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        // r--> number of rows.
        int r = mat.size();
        // c--> number of columns
        int c = mat[0].size();
        
        // prefix--> prefix sum of each row.
        int prefix[r][c];
        
        // ans will hold the submatrix sum.
        vector<vector<int>> ans;
        
        // prefix sum of each row.
        for(int i=0;i<r;i++){
            int cur_sum = 0;
            vector<int> row;
            for(int j=0;j<c;j++){
                cur_sum+=mat[i][j];
                prefix[i][j] = cur_sum;
                row.push_back(0);
            }
            ans.push_back(row);
        }
        
        // using prefix sum of from i-K to i+K of valid rows for each item. 
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int r1 = max(0,i-K);
                int r2 = min(r-1,i+K);
                int c1 = max(0,j-K);
                int c2 = min(c-1,j+K);
                int cnt = 0;
                for(int k=r1;k<=r2;k++){
                    cnt+=(prefix[k][c2]-prefix[k][c1]+mat[k][c1]);
                }
                ans[i][j] = cnt;
            }
        }
        
        return ans;
    }
};
