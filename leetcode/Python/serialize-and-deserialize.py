# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        final_str = f"{root.val}"
        final_str += f"[{self.serialize(root.left)}]"
        final_str += f"[{self.serialize(root.right)}]"
        return final_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(f"Data: {data}")
        if data == "":
            return None
        
        num =""
        left_found = False
        count = 0
        left_finished = False
        left = ""
        right = ""
        for letter in data[:-1]:
            if letter == "[":
                if count == 0:
                    left_found = True
                    count = 1
                    continue
                else:
                    count += 1
    
            elif letter == "]":
                count -= 1
                if count == 0:
                    left_finished = True
                    continue
            elif not left_found:
                num += letter
                continue

            if not left_finished:
                left += letter
            else: 
                right += letter

        #print(num, left, right)
        if num == "":
            return None
        else:
            return TreeNode(val=int(num), left=self.deserialize(left), right=self.deserialize(right))
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))