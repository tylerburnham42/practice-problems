# Leetcode 2/1/21
# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        # Deal with the single item list case
        if not head.next:
            return head
        
        # Get the new head at the start since we have at least 2 items.
        new_head = head.next
        current = head
        
        # Loop over each node
        while current:
            current = self.insert(current)
            
        return new_head
        
    def insert(self, to_insert):
        current = to_insert
        next_index = None
        
        # If next node is the last return None
        if not current.next:
            return None
        
        elif not current.next.next:
            before_insert = current.next
            after_insert = None
            
            before_insert.next = current
            current.next = after_insert
            return None
        
        elif not current.next.next.next:
            before_insert = current.next
            after_insert = current.next.next

            before_insert.next = current
            current.next = after_insert
            return None
        
        else:
            before_insert = current.next
            after_insert = current.next.next.next
            next_node = current.next.next

            before_insert.next = current
            current.next = after_insert
            return next_node