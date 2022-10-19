#Single Linked List
# Create Node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        # Initialize data structure here.
        self.head = None # head always indicates the linkedlist starting point
        self.size = 0    
        
    def get(self, index: int) -> int:
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
        i = 0
        while i< index:
            curr = curr.next
            i+=1
        return curr.val
    
    def addAtHead(self, val: int) -> None:
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

    # See the whole linked list   

    # def print(self): 
    #     curr = self.head
    #     if curr is None:
    #         print("Empty LinkedList!")
            
    #     myll_srt = ""
    #     while curr:
    #         myll_srt += str(curr.val) + "-->"
    #         curr = curr.next
    #     print(myll_srt)
    
        
    def addAtTail(self, val: int) -> None:
        """
        append a node of vale val to the last element of the linkedlist.
        :type val: int
        :return type: void
        
        """
        
        curr = self.head
        if curr is None:
            # when empty node
            self.head = Node(val)
        else:
            while curr.next: # it is important, hey it is curr.next
                curr = curr.next
            curr.next = Node(val)
            
        self.size += 1
        
        
    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of val before the index-th node in the linkedlist
        If index equals to the length of linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :return type: void
        
        """
        
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            
            i = 0
            while i < (index-1):
                curr = curr.next
                i += 1
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size += 1
            
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if index is valid.
        :type index: int
        :return type: void
        
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head

        if index == 0:
            self.head = curr.next

        else:
            i = 0
            while i < (index-1):
                curr = curr.next
                i += 1
            curr.next = curr.next.next

        self.size -= 1
        

# if __name__=="__main__":
#     myll = MyLinkedList()
#     myll.addAtHead(1)
#     myll.addAtHead(2)
#     myll.addAtHead(5)
#     print(myll.get(0))
#     myll.print()
#     # 5-->2-->1-->
#     myll.addAtTail(15)
#     myll.addAtTail(20)
#     myll.print()
#     # 5-->2-->1-->15-->20-->
#     myll.addAtIndex(3,23)
#     myll.print()
#     # 5-->2-->1-->23-->15-->20-->
#     myll.deleteAtIndex(2)
#     myll.print()
#     # 5-->2-->23-->15-->20-->
        


#     # Your MyLinkedList object will be instantiated and called as such:
#     # obj = MyLinkedList()
#     # param_1 = obj.get(index)
#     # obj.addAtHead(val)
#     # obj.addAtTail(val)
#     # obj.addAtIndex(index,val)
#     # obj.deleteAtIndex(index)