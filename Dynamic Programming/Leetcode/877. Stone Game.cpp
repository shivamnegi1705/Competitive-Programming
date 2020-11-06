// Question Link:- https://leetcode.com/problems/stone-game/

class Solution {
public:
    // n--> size of pile
    int n;
    // dp[left index][right index]
    int dp[505][505];
    int func(int l, int r,vector<int> &piles){
        // when no pile is left.
        if(l>r){
            return 0;
        }
        // if dp is set then return.
        if(dp[l][r]!=-1){
            return dp[l][r];
        }
        // choice1 -> player1 takes lth pile and player2 takes l+1 th pile.
        int ch1 = piles[l]+func(l+2,r,piles);
        
        //choice2 -> player1 takes rth pile and player2 takes r-1th pile.
        int ch2 = piles[r]+func(l,r-2,piles);
        
        // choice3 -> player1 takes lth pile and player2 takes rth pile.
        int ch3 = piles[l]+func(l+1,r-1,piles);
        
        // choice4 -> player1 takes rth pile and player2 takes lth pile.
        int ch4 = piles[r]+func(l+1,r-1,piles);
        
        // set max of all four choices.
        return dp[l][r] = max(ch1,max(ch2,max(ch3,ch4)));
    }
    bool stoneGame(vector<int>& piles) {
        n = piles.size();
        // initial dp set to -1.
        memset(dp,-1,sizeof(dp));
        // total sum of stones.
        int total = 0;
        for(int i=0;i<n;i++){
            total+=piles[i];
        }
        // player1 max score
        int pl1 = func(0,n-1,piles);
        int pl2 = total-pl1;
        if(pl1>pl2){
            return true;
        }
        return false;
    }
};
