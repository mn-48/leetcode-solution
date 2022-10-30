# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def index(node):
            if not node:
                return 0
            i = index(node.next)+1
            
            if i>n:
                node.next.val = node.val
            return i
        
        index(head)
        return head.next