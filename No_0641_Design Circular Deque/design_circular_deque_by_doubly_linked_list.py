class Node:
    
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
        self.capacity = k
        self.size = 0
        
        head_node = Node( 0 )
        
        cur = head_node
        
        for i in range(1,k):
            
            # build double linkage
            cur.next = Node(i)
            cur.next.prev = cur
            
            cur = cur.next
            
        # build double linkage
        cur.next = head_node
        head_node.prev = cur
        
        # initialization for front and rear
        self.front = head_node.prev
        self.rear = head_node
        
        
        
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            
            self.front.value = value
            self.front = self.front.prev
            
            self.size += 1
        
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        
        if self.size+1 <= self.capacity:
            
            self.rear.value = value
            self.rear = self.rear.next
            
            self.size += 1
        
            return True
        
        else:
            return False
        
        
        
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if self.size != 0:
            
            self.front = self.front.next
            self.size -= 1
            return True
        
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if self.size != 0:
            
            self.rear = self.rear.prev
            self.size -= 1
            return True
        
        else:
            return False        
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        
        if self.size != 0:
            return self.front.next.value
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        
        if self.size != 0:
            return self.rear.prev.value
        else:
            return -1
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.size == self.capacity



# Time Complexity:
#
# __init__      : O( k )
#
# deleteFront   : O( 1 )
#
# getFront      : O( 1 )
#
# insertFront   : O( 1 )
#
# deleteLast    : O( 1 )
#
# getRear       : O( 1 )
#
# insertLast    : O( 1 )
#
# isFull        : O( 1 )
#
# isEmpty       : O( 1 )



# Space Complexity:
#
# __init__      : O( k )
#
# deleteFront   : O( 1 )
#
# getFront      : O( 1 )
#
# insertFront   : O( 1 )
#
# deleteLast    : O( 1 )
#
# getRear       : O( 1 )
#
# insertLast    : O( 1 )
#
# isFull        : O( 1 )
#
# isEmpty       : O( 1 )