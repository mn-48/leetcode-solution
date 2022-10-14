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
        
        # Time complexity O(n)
        # Space complexity O(1)
        """
        
        if index < 0 or index >= self.size:
            return -1
        
        # When LinkedList is empty return -1
        if self.head is None:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the LinkedList.
        After the insertion, new node will be the first node of the LinkedList.
        :type val: int
        :return type: void
        
        """
        
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        # print("head", self.head.val)
        
    def print(self):
        curr = self.head
        if curr is None:
            print("Empty LinkedList!")
            
        myll_srt = ""
        while curr:
            myll_srt += str(curr.val) + "-->"
            curr = curr.next
        print(myll_srt)
        
        
    
    
    
if __name__=="__main__":
    myll = MyLinkedList()
    myll.addAtHead(1)
    myll.addAtHead(2)
    myll.addAtHead(5)
    print(myll.get(0))
    myll.print()
    
        