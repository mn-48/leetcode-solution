# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow_pointer = head
            fast_pointer = head.next

            while slow_pointer is not fast_pointer:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            return True
        except:
            return False
        