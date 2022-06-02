# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:

        self.goodNodesCounter(root, float('-inf'))
        return self.count
            
    def goodNodesCounter(self, root: TreeNode, most = 0) -> int:
        if root is None:
            return
            
        #print(root.val, most)
        if root.val >= most:
            #print("counted")
            most = root.val
            self.count += 1
            
        
        #print("Count:", self.count)
        
        self.goodNodesCounter(root.left, most)
        self.goodNodesCounter(root.right, most)