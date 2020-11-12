// Question Link:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minprice = INT_MAX;
        int mex = 0;
        for(int i=0;i<prices.size();i++){
            if(prices[i]<minprice){
                minprice = prices[i];
            }
            else if(prices[i]-minprice > mex){
                mex = prices[i]-minprice;
            }
        }
        return mex;
    }
};
