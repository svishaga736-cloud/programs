# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            
            # Create new node and move current pointer
            current.next = ListNode(val)
            current = current.next
            
            # Move l1 and l2 pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
