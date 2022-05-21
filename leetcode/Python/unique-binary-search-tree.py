# Unique Binary Search Trees II #95
# Need to revisit
# Solved with help via recursion
# 5-21-2022
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0:
            return []
        
        return self.buildTree(1, n)
      

        
    def buildTree(self, start, end) -> List[Optional[TreeNode]]:
        trees = []
        
        for val in range(start, end + 1):
            for left in self.buildTree(start, val-1):
                for right in self.buildTree(val+1, end):
                    trees.append(TreeNode(val,left,right))
                    
        return trees or [None]