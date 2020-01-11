'''

This file is just a practice of native deque in Python.

Problem description asks us not to use built-in queue library

'''



class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

        self.circular_q = collections.deque()
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.circular_q) != self.capacity:
            
            self.circular_q.append( value )
            
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.circular_q) != 0:
        
            self.circular_q.popleft()
            
            return True
        else:
            return False
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.circular_q) != 0:
            return self.circular_q[ 0 ]
        else:
            return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.circular_q) != 0:
            return self.circular_q[ -1 ]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.circular_q) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.circular_q) == self.capacity   



# Time Complexity:
#
# __init__  : O( k )
#
# deQueue   : O( 1 )
#
# enQueue   : O( 1 )
#
# Fonrt     : O( 1 )
#
# Rear      : O( 1 )
#
# isEmpty   : O( 1 )
#
# isFull    : O( 1 )



# Space Complexity:
#
# __init__  : O( k )
#
# deQueue   : O( 1 )
#
# enQueue   : O( 1 )
#
# Fonrt     : O( 1 )
#
# Rear      : O( 1 )
#
# isEmpty   : O( 1 )
#
# isFull    : O( 1 )