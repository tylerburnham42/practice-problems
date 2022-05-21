# Binary Tree InOrder Treversal #94
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Solved 5-21-2022
# Solved with recursion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        values = []
        if(root.left):
            values.extend(self.inorderTraversal(root.left))

        values.append(root.val)

        if(root.right):
            values.extend(self.inorderTraversal(root.right))
        
        return values