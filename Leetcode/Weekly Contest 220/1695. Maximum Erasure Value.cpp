//Question Link:- https://leetcode.com/problems/maximum-erasure-value/

class Solution {
public:
    int maximumUniqueSubarray(vector<int>& arr) {
        int i = 0;
        int j = 1;
        int s = arr[0];
        int mex = s;
        int n = arr.size();
        vector<int> cnt(10005,0);
        cnt[arr[0]]+=1;
        while(i<n-1 && j<n){
            const bool is_in = cnt[arr[j]]==1;
            if(!is_in){
                s+=arr[j];
                mex = max(mex,s);
                cnt[arr[j++]]+=1;
            }
            else{
                s-=arr[i];
                cnt[arr[i++]]-=1;
            }
        }
        return mex;
    }
};
