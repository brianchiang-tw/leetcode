'''

This file is just a practice of native deque in Python.

Problem description asks us not to use built-in duque library

'''

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.circular_deque = collections.deque()
        self.capacity = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        
        if len( self.circular_deque) != self.capacity:
            self.circular_deque.appendleft( value )
            return True
        
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        
        if len( self.circular_deque) != self.capacity:
            self.circular_deque.append( value )
            return True
    
        else:
            return False
        
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if len( self.circular_deque ) != 0:
            self.circular_deque.popleft()
            return True
        
        else:
            return False

        
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        
        if len( self.circular_deque ) != 0:
            self.circular_deque.pop()
            return True
        
        else:
            return False

        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        
        if len( self.circular_deque ) != 0:
            return self.circular_deque[0]
        
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

        if len( self.circular_deque ) != 0:
            return self.circular_deque[-1]
        
        else:
            return -1        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return len( self.circular_deque ) == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return len( self.circular_deque ) == self.capacity



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