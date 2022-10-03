# [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
# Time complexity O(n)
# Space complexity O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_itr = head
        slow_itr = head
 
        while fast_itr and fast_itr.next:
            fast_itr = fast_itr.next.next
            slow_itr = slow_itr.next
          
        return slow_itr
            
        
