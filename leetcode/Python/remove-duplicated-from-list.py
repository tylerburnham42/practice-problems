# Remove duplicated from list. #83
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Solved 5-23-2022
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        last_node = head
        current_node = head.next
        
        
        while (current_node):
            #print(last_node, current_node)
            if current_node.val == last_node.val:
                last_node.next = current_node.next
            else:
                last_node = current_node  
            
            current_node = current_node.next
            
        return head