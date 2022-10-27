# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        n = 1
        while curr.next:
            n+=1
            curr = curr.next


        k = k%n
        if not k:
            return head

 
        middle = head
   
        for i in range(n-k-1):
            middle = middle.next
        
        new_head = middle.next
        curr.next = head
        middle.next = None

        return new_head
    
    
# Time complexity O(n)
# Space complexity O(1)
