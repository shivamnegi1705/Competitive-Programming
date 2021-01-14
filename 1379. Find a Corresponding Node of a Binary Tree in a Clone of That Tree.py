# Question Link:- https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = None
        def func(node):
            nonlocal ans
            if node==None:
                return
            func(node.left)
            func(node.right)
            if node.val==target.val:
                ans = node
        func(cloned)
        return ans
