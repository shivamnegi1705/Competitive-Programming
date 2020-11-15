// Question Link:- https://leetcode.com/problems/counting-bits/
class Solution {

public:

    vector<int> countBits(int num) 

    {

        vector<int> a(num+1);

        a[0] = 0;

        

        for(int i = 1 ; i <= num ; i++) 

        {

            if(i%2 == 0) a[i] = a[i >> 1];

            else a[i] = a[i >> 1] + 1;

        }

        return a;

    }

};
