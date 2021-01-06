// Question Link:- https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorder(TreeNode *root){
        if(root==NULL){
            vector<int> arr(3,-1);
            return arr;
        }
        vector<int> left = postorder(root->left);
        vector<int> right = postorder(root->right);
        vector<int> ans(3,0);
        ans[0] = left[1]+1;
        ans[1] = right[0]+1;
        ans[2] = max(ans[0],max(ans[1],max(left[2],right[2])));
        return ans;
        
    }
    int longestZigZag(TreeNode* root) {
        vector<int> ans = postorder(root);
        return ans[2];
    }
};
