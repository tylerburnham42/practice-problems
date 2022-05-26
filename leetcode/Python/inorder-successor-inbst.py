# 285. Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/
# Solved 5-26-2022 - Should review.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if root == None:
            return
        
        #print(root.val, p.val)
        if (root.val > p.val):
            return self.inorderSuccessor(root.left, p) or root
        else:
            return self.inorderSuccessor(root.right, p)