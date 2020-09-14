# Leetcode 7/16
# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        current = l3

        while l2 != None or l1 != None:
            print(l1, "\n", l2,"\n", current, "\n\n")
            if l2 == None:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1 == None:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
                
            current = current.next
            
        return l3.next
