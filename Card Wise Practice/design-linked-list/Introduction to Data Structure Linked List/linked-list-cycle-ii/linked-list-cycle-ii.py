# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer:
                break;
        else: 
            return None
        while head != slow_pointer:
            slow_pointer = slow_pointer.next
            head = head.next
        # print(head.val)
        return head
            
# Time complexity O(n)
# Space complexity O(1)
        
       
        
        