class Node:

    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None    



class MyLinkedList:


        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head = None
        self.tail = None
        self.size = 0

        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        # valid index checking
        if index >= self.size or index < 0:
            return -1
        
        
        if self.head is None:
            return -1
        
        elif index == 0:
            return self.head.val
        
        else:
            
            current = self.head
            while( current.next is not None and index ):
                current = current.next
                index -= 1
            
            
            return current.val

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node( val )
        
        # update size of linklist
        self.size += 1
        
        
        if self.head is None:
            # if linklist is empty, directly make new node as head node as well as tail node
            self.head = new_node
            self.tail = new_node
        
        else:
        
            # create double link between new node and original head node
            new_node.next = self.head
            self.head.prev = new_node
            
            # update new node as new head node
            self.head = new_node
            
            
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        new_node = Node( val )
        
        # update size of linklist
        self.size += 1
        
        if self.tail is None:
            # if linklist is empty, directly make new node as tail node as well as head node
            self.tail = new_node
            self.head = new_node
        
        else:
            
            # create double link between new node and original tail node
            new_node.prev = self.tail
            self.tail.next = new_node
            
            # update new node as new tail node
            self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index > self.size:
            
            # Index is greater the length, the node will not be inserted.
            pass
            return
        
        new_node = Node( val )
        

        
        if self.head is None and index == 0:
            
            # if linklist is empty, directly make new node as tail node as well as head node
            self.head = new_node
            self.tail = new_node
            
        elif self.head is not None and index == 0:
            
            # create double link between new node and original head node
            new_node.next = self.head
            self.head.prev = new_node
            
            # update new node as new head node
            self.head = new_node
            
            
        elif (index == self.size) and (None != self.tail ) :
            
            # create double link between new node and original tail node
            new_node.prev = self.tail
            self.tail.next = new_node
            
            # update new node as new tail node
            self.tail = new_node
        
        else:
            #print("here")
            current = self.head
            while( current.next is not None and (index-1) ):
                current = current.next
                index -= 1
            
            # record next of new node
            next_of_new_node = current.next

            # create double link between new node and new node's prev
            current.next = new_node
            new_node.prev = current

            # create double link between new node and new node's next
            new_node.next = next_of_new_node
            next_of_new_node.prev = new_node

        # update size of linklist
        self.size += 1        
                
        return
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or index < 0:
            return 
        
        if index == 0 :
            
            # Record new head
            new_head = self.head.next
            
            if new_head is not None:
                # delete double link between new head and old head
                self.head.next = None
                new_head.prev = None
            else:
                # delete single link of old head
                self.head.next = None
                
                # now it is a empty link list
                self.tail = None
            
            # update new haed
            self.head = new_head
            
            # update size of linklist
            self.size -= 1
        
        elif index == (self.size - 1) :
            
            # Record new tail
            new_tail = self.tail.prev
            
            if new_tail is not None:
                # delete double link between new tail and old tail
                self.tail.prev = None
                new_tail.next= None
            else:
                # delete single link of old tail
                self.tail.prev = None
            
                # noe it is a empty link list
                self.head = None
            
            # update new tail
            self.tail = new_tail
            
            # update size of linklist
            self.size -= 1
            
        else:
            
            current = self.head
            while( current.next is not None and index ):
                current = current.next
                index -= 1
                
            # Record prev and next of deleted node
            _prev = current.prev
            _next = current.next
            
            # create double link between _prev and _next
            _prev.next = _next
            _next.prev = _prev
            
            # delete double link of deleted node
            current.prev = None
            current.next = None
            
            # update size of linklist
            self.size -= 1
    


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
            print("size = {}, Linked-list : {}".format( self.size, travesal ) )
            

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