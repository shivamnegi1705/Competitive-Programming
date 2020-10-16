// Question Link:- https://leetcode.com/problems/count-all-possible-routes/
class Solution {
public:
    int ans[102][202];
    int n;
    int fin;
    const int mod = 1000000007;
    int func(int c,int f,vector<int>&arr){
        if(ans[c][f]!=-1){
            return ans[c][f];
        }
        int cnt = 0;
        if(c==fin){
            cnt++;
        }
        for(int i=0;i<n;i++){
            if(i!=c){
                int req = abs(arr[c]-arr[i]);
                if(req<=f){
                    cnt = (cnt*1LL +func(i,f-req,arr))%mod;
                }
            }
        }
        return ans[c][f] = cnt;
    }
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        n = locations.size();
        fin = finish;
        memset(ans,-1,sizeof(ans));
        return func(start,fuel,locations);
        
    }
};
