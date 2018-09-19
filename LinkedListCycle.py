# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        kossop = head
        khorgos = head
        while (kossop and khorgos and khorgos.next):
            kossop = kossop.next
            khorgos = khorgos.next.next
            if khorgos == kossop:
                return True
        return False