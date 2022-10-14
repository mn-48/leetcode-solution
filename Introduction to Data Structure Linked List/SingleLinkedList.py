# Create Node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        # Initialize data structure here.
        self.head = None
        self.size = 0    
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. 
        If index is invalid return -1
        """
        
        if index < 0 or index >= self.size:
            return -1
        # When LinkedList is empty
        
        if self.head is None:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    
        