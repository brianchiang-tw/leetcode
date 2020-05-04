'''

Description:

Design Linked List
Solution
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 

Example:

Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
 

Constraints:

0 <= index,val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.

'''



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

        ### trace and debug
        #self.print_linked_list()
        
        
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

        ### trace and debug
        #self.print_linked_list()            
        
        
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

        ### trace and debug
        #self.print_linked_list()
        

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

        ### trace and debug
        #self.print_linked_list()            
            
            
    def print_linked_list(self):
        
        cur = self.head
        
        while cur:
            print( f' {cur.val} -> ', end = '')
            cur = cur.next
        
        print('None\n')
        
        return
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



def test_bench():


    # expected output:
    '''
    2
    3
    '''

    linkedList = MyLinkedList()     # Initialize empty LinkedList
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)     # linked list becomes 1->2->3
    print( linkedList.get(1) )      # returns 2
    linkedList.deleteAtIndex(1)     # now the linked list is 1->3
    print( linkedList.get(1) )      # returns 3



if __name__ == '__main__':

    test_bench()    