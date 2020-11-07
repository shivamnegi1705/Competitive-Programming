// Question Link:- https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        // r--> number of rows.
        int r = mat.size();
        // c--> number of columns
        int c = mat[0].size();
        
        // prefix--> prefix sum of each row.
        int prefix[r][c];
        
        for(int i=0;i<r;i++){
            int cnt = 0;
            for(int j=c-1;j>=0;j--){
                if(mat[i][j]==1){
                    cnt+=1;
                }
                else{
                    cnt = 0;
                }
                prefix[i][j] = cnt;
            }
        }
        
        int ans = 0;
        
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int row = 1;
                int col = prefix[i][j];
                for(int k=i;k<r;k++){
                    if(mat[k][j]==0){
                        break;
                    }
                    col = min(col,prefix[k][j]);
                    ans+=col;
                    row+=1;
                }
            }
        }
        return ans;
    }
};
