// Question Link:- https://leetcode.com/problems/minimum-incompatibility/

class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        int n = nums.size();
        int b = n/k;
        sort(nums.begin(),nums.end());
        vector<int> mapper(1<<16,-1);
        
        for(int i=0;i<(1<<n);i++){
            if(__builtin_popcount(i)==b){
                vector<int> selected;
                int cnt = 0;
                for(int j=0;j<n;j++){
                    if(i&(1<<j)){
                        cnt+=(1<<j);
                        selected.push_back(nums[j]);
                    }
                }
                int f = 0;
                for(int j=0;j<selected.size()-1;j++){
                    if(selected[j]==selected[j+1]){
                        f = 1;
                    }
                }
                if(f==1){
                    continue;
                }
                int amplitude = selected.back()-selected[0];
                mapper[cnt] = amplitude;
            }
        }
        int inf = 1e8;
        vector<int> dp(1<<n,inf);
        dp[0] = 0;
        for(int i=1;i<(1<<n);i++){
            int mask = i;
            int mask2 = mask;
            while(mask2>0){
                if(mapper[mask2]!=-1){
                    dp[mask] = min(dp[mask],dp[mask^mask2]+mapper[mask2]);
                }
                mask2 = (mask2-1)&mask;
            }
        }
        if(dp.back()==inf){
            return -1;
        }
        return dp.back();
    }
};
