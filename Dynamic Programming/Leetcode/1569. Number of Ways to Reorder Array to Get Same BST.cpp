// Question Link:- https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

#define ll long long int
class Solution {
public:
    ll fac[2005];
    ll n;
    const ll mod = 1000000007;
    
    ll modularexpo(ll x,ll n,ll mod){
        ll res = 1;
        while(n>0){
            if(n%2==1){
                res = (res*x)%mod;
            }
            x = (x*x)%mod;
            n = n/2;
        }
        return res;
    }
    
    ll helper(int m, int r) {
        ll x = fac[m+r];
        ll y = (fac[m] * fac[r])%mod;
        y = modularexpo(y,mod-2,mod);
        return (x*y)%mod;
    }
    
    template <typename T>
    int func(vector<T>& arr){
        ll q = arr.size();
        if (arr.size() < 2)
            return 1;
        vector<T> left, right;
        for (int i = 1; i < q; i++){
            if (arr[i] > arr[0])
                right.push_back(arr[i]);
            else
                left.push_back(arr[i]);
        }
        ll val1 = ((func(left)%mod * func(right)%mod)%mod);
        ll a = left.size();
        ll b = right.size();
        ll val2 = helper(a,b);
        return (val1*val2)%mod;
    }
    
    int numOfWays(vector<int>& nums) {
        n = nums.size();
        fac[0] = 1;
        for(ll i=1;i<2*(n+1);i++){
            fac[i] = (fac[i-1]*i)%mod;
        }
        return func(nums)-1;
        
    }
};
