# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous_head = ListNode(None)
        
        while head:
            previous_head.next, head.next , head = head, previous_head.next, head.next 
            
        return previous_head.next
        