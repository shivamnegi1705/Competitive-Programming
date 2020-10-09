# Question Link:- https://leetcode.com/problems/even-odd-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        # checking level 0 node (should have odd value)
        if(root.val)%2==0:
            # if root has even value then it's not a Even-Odd Tree.
            return False
        
        # applying BFS to traverse whole Tree Level by level.
        queue = [root]
        valid = True
        next_level = []
        values = []
        level_no = 1
        
        while queue!=[]:
            cur_node = queue[0]
            queue.pop(0)
            
            # checking Left node of current node.
            if cur_node.left!=None:
                next_level.append(cur_node.left)
                values.append(cur_node.left.val)
            
            # checking Right node of current node.
            if cur_node.right!=None:
                next_level.append(cur_node.right)
                values.append(cur_node.right.val)
            
            # it means we have explored the current level completely.
            if queue==[]:
                # update the unexplored level.
                queue = next_level[::]
                next_level = []
                
                # odd level should have even values strictly decreasing.
                if level_no%2!=0:
                    mex = 10**7
                    for i in values:
                        if i<mex and i%2==0:
                            mex = i
                        else:
                            valid = False

                # even level should have odd values strictly increasing.
                else:
                    mn = 0
                    for i in values:
                        if i>mn and i%2!=0:
                            mn = i
                        else:
                            valid = False

                values = []
                level_no+=1
                
        return valid
