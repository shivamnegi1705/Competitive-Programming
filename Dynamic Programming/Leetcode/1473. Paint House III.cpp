// Question Link:- https://leetcode.com/problems/paint-house-iii/

class Solution {
public:
    int dp[105][25][105];
    int func(int ind, int prev, int k,vector<int> &arr,vector<vector<int>> &cost,int &m,int &n,int &grps){
        if(ind==m){    
            if(k!=grps){
                return 10000000;
            }
            else{
                return 0;
            }
        }
        if(dp[ind][prev][k]!=-1){
            return dp[ind][prev][k];
        }
        int ans = 10000000;
        if(arr[ind]!=0){
            if(prev==arr[ind]){
                ans = min(ans,func(ind+1,prev,k,arr,cost,m,n,grps));
            }
            else{
                ans = min(ans,func(ind+1,arr[ind],k+1,arr,cost,m,n,grps));
            }
        }
        else{
            for(int i=1;i<=n;i++){
                if(prev==i)
                    ans = min(ans,cost[ind][i-1]+func(ind+1,prev,k,arr,cost,m,n,grps));
                else
                    ans = min(ans,cost[ind][i-1]+func(ind+1,i,k+1,arr,cost,m,n,grps));
            }
        }
        return dp[ind][prev][k] = ans;
    }
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        memset(dp,-1,sizeof(dp));
        int ans = func(0,21,0,houses,cost,m,n,target);
        if(ans==10000000)
            return -1;
        return ans;
    }
};
