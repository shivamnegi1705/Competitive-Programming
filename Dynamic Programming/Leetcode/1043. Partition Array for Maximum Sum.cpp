// Question Link:- https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
public:
    // n--> size of array.
    int n;
    // lookup table --> max for all subarrays.
    int lookup[505][505];
    // dp--> to hold intermediate state ans.
    // dp[right pointer][length]
    int dp[505][505];
    
    //
    int func(int r,int length,int &k){
        // right pointer at the end.
        if(r==n-1){
            // left pointer = right pointer - length + 1.
            int l = n-1-length+1;
            return length*lookup[l][r];
        }
        if(dp[r][length]!=-1){
            return dp[r][length];
        }
        int ch1 = 0, ch2 = 0;
        // left pointer = right pointer - length + 1.
        int l = r-length+1;
        // ch1 --> end current subarray at point r
        ch1 = lookup[l][r]*length + func(r+1,1,k);
        
        // if it is possible to extend current subarray.
        if(length+1<=k){    
            int ch2 = func(r+1,length+1,k);
        }
        
        // set max of both choices.
        return dp[r][length] = max(ch1,ch2);
    }
    int maxSumAfterPartitioning(vector<int>& arr, int k){
        n = arr.size();
        // initial dp of -1.
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<n;i++){
            int mex = arr[i];
            for(int j=i;j<n;j++){
                mex = max(mex,arr[j]);
                lookup[i][j] = mex;
            }
        }
        return func(0,1,k);
    }
};
