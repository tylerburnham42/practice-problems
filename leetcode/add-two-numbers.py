# Leetcode 7/5/2020
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        out_start = ListNode()
        out = out_start
        
        while l1 != None or l2!= None:
            
            #If l1 and l2 are not None
            if l1 != None and l2 != None:
                out.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            # If l1 is not None
            elif l1 != None:
                out.val += l1.val
                l1 = l1.next
            
            # if l2 is not None
            else:
                out.val += l2.val
                l2 = l2.next
                
            carry = int(out.val/ 10)
            out.val = out.val % 10
            
            if l1 != None or l2 != None:
                out.next = ListNode(carry)
                out = out.next
            else:
                if carry:
                    out.next = ListNode(carry)
                    out = out.next
                    
        return out_start