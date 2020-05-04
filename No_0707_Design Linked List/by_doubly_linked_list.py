class ListNode():
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index < 0 or index >= self.length:
            return -1
        
        cur = self.head
        
        while index != 0:
            
            cur = cur.next
            index -= 1
            
        return cur.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        new_node = ListNode( val )
        
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node
        
        self.head = new_node
               
        self.length += 1
        
        if self.length == 1:
            self.tail = new_node


        
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        new_node = ListNode( val )
        
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node
        
        self.length += 1
        
        if self.length == 1:
            self.head = new_node

          
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index < 0 or index > self.length:
            return
        
        elif index == 0:
            self.addAtHead( val )
        
        elif index == self.length:
            self.addAtTail( val )
            
        else:
                
            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            new_node = ListNode( val )

            new_node.next = cur.next
            cur.next.prev = new_node

            cur.next = new_node
            new_node.prev = cur
            
            self.length += 1


        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index >= self.length:
            return
        
        elif index == 0:
            
            if self.head.next:
                self.head.next.prev = None
                
            self.head = self.head.next
            
            self.length -= 1
            
            if self.length == 0:
                self.tail = None
        
        elif index == self.length-1:
            
            if self.tail.prev:
                self.tail.prev.next = None
            
            self.tail = self.tail.prev
            
            self.length -= 1
            
            if self.length == 0:
                self.head = None
            
        else:
                
            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur
            
            self.length -= 1
    


    # _print is a support function for debugging and tracing
    def _print(self):

        if self.head is None:
            print("Empty linked list")
        else:
            travesal = []
            current = self.head
            while( current is not None ):
                travesal.append( current.val )
                current = current.next

            print()
            print("head = {}, tail = {}".format( self.head.val, self.tail.val ) )
            print("size = {}, Linked-list : {}".format( self.length, travesal ) )
            

        return

# N : the total nodes of linked-list

## Time Complexity : O( N )
#
# addAtHead() costs O( 1 )
# addAtIndex() costs O( N )
# addAtTail() costs O( 1 )
# deleteAtIndex() costs O( N )
# get() costs O( N )
# __init__() costs O( 1 )
#
# In summary, the time complexity of linked-list is O( N )


## Space Complexity : O( N )
#
# The major overhead is to mainain a linklist of N node, this takes O( N )
#
# Also, there is some temporary vairable for node opeation and link update takes O( 1 )
# In summary, the space complexity of linked-list is O( N )


def test_bench():

    linklist = MyLinkedList()
    linklist.addAtHead(7)
    linklist.addAtHead(2)
    linklist.addAtHead(1)
    linklist.addAtIndex(3, 0)
    linklist.deleteAtIndex(2)
    linklist.addAtHead(6)
    linklist.addAtTail(4)
    linklist.get(4)
    linklist.addAtHead(4)
    linklist.addAtIndex(5, 0)
    linklist.addAtHead(6)


# # expected output:
# head = 6, tail = 4
# size = 8, Linklist : [6, 4, 6, 1, 2, 0, 0, 4]

    linklist._print()
    return



if __name__ == '__main__':

    test_bench()