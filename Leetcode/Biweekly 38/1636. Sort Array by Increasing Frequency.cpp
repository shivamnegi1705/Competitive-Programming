// Question Link:- https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> mapper;
        for(int x: nums)
            mapper[x]++;
        sort(begin(nums), end(nums),[&](int a, int b){
            if(mapper[a] != mapper[b])
                return mapper[a] < mapper[b];
            else
                return a > b;
        });
        return nums;
        
    }
};
