# Question Link:- https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            
            nonlocal ans
            
            # Null Node return []
            if node==None:
                return []
            
            # Leaf node
            if node.left==None and node.right==None:
                return [1]
            
            # left half list containing distances from current node to all leaves in left half.
            left_half = dfs(node.left)
            
            # right half list containing distances from current node to all leaves in right half
            right_half = dfs(node.right)
            
            # taking each pair and check distance sum 
            for i in left_half:
                for j in right_half:
                    if i+j<=distance:
                        ans+=1
                        
            # updating distances
            new_dist = []
            for i in left_half:
                if i+1<distance:
                    new_dist.append(i+1)
            
            for i in right_half:
                if i+1<distance:
                    new_dist.append(i+1)
            
            return new_dist
        
        ans = 0
        dfs(root)
        return ans
