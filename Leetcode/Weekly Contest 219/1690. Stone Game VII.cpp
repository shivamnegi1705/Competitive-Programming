// Question Link:- https://leetcode.com/problems/stone-game-vii/

class Solution {
public:
    int n;
    int precalc[1001][1001];
    int dp[1001][1001][2];
    
    int func(int i,int j,int f,vector<int>& arr){
        if(i==j){
            return 0;
        }
        if(dp[i][j][f]!=1e7){
            return dp[i][j][f];
        }
        int ans;
        if(f==0){
            ans = -1e7;
            ans = max(ans,precalc[i+1][j]+func(i+1,j,1,arr));
            ans = max(ans,precalc[i][j-1]+func(i,j-1,1,arr));
        }
        else{
            ans = 1e7;
            ans = min(ans,-precalc[i+1][j]+func(i+1,j,0,arr));
            ans = min(ans,-precalc[i][j-1]+func(i,j-1,0,arr));
        }
        return dp[i][j][f] = ans;
    }
    
    int stoneGameVII(vector<int>& stones) {
        n = stones.size();
        for(int i=0;i<n;i++){
            int s = 0;
            for(int j=i;j<n;j++){
                s+=stones[j];
                precalc[i][j] = s;
            }
        }
        for(int i=0;i<1001;i++){
            for(int j=0;j<1001;j++){
                for(int k=0;k<2;k++){
                    dp[i][j][k] = 1e7;
                }
            }
        }
        return func(0,n-1,0,stones);
        
    }
};
