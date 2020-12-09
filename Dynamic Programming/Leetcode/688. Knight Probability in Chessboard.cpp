// Question Link:- https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution {
    double arr[30][30][110];
double dfs(int i, int j, int N, int moves)
{
    if(i<0 or j<0 or i>=N or j>=N)
        return 0.0;
    if(moves==0)
        return 1.0;
    if(arr[i][j][moves]>=0.0)
        return arr[i][j][moves];
    
    vector<pair<int,int>>vec={ {-2,1}, {-2,-1}, {-1,2}, {-1,-2}, {1,2}, {1,-2},
                              {2,1}, {2,-1} };
    double ans=0.0;
    for(int k=0;k<8;k++)
    {
        int r= i + vec[k].first;
        int c= j + vec[k].second;
        ans+=dfs(r,c,N,moves-1);
    }
    
    return arr[i][j][moves]=(double)(ans*0.125);
    
    
}
public:
    double knightProbability(int N, int K, int r, int c) {
        memset(arr,-1.0,sizeof(arr));
        return dfs(r,c,N,K);
    }
};
