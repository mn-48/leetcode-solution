# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_linked_list(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start

        while result and second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next 

        # restore the list
        first_position.next = self.reverse_linked_list(second_position)
        return result


    # traverse slow pointer to half of the linkedlist 
    #
    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next 
        return slow

    # reverse second half
    def reverse_linked_list(self, head):
        previous = None
        current = head

        while current is not None:
            next_node = current.next 
            current.next = previous
            previous = current
            current = next_node
        return previous
        
       