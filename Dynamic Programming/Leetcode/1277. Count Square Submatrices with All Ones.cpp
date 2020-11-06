// Question Link:- https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        // r--> number of rows.
        int r = matrix.size();
        // c--> number of columns.
        int c = matrix[0].size();
        
        // for any (i,j)--> prefix[i][j] will hold how many 1 are there from (i,j)-->(i,j+1)-->(i,j+2)..
        int prefix[r][c];
        
        for(int i=0;i<r;i++){
            int cnt = 0;
            for(int j=c-1;j>=0;j--){
                if(matrix[i][j]==1){
                    cnt+=1;
                }
                else{
                    cnt = 0;
                }
                prefix[i][j] = cnt;
            }
        }
        
        // ans--> hold the count squares.
        int ans = 0;
        
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int side = 1;
                int pre = prefix[i][j];
                for(int k=i;k<r;k++){
                    // if 0 is encounter break
                    if(matrix[k][j]==0){
                        break;
                    }
                    pre = min(prefix[k][j],pre);
                    // other side(pre) of square is less than side then break 
                    if(pre<side){
                        break;
                    }
                    ans+=1;
                    side+=1;
                }
            }
        }
        return ans;
        
    }
};
