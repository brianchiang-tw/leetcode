'''

Description:

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.

'''



class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

        self.circular_q = [ 0 ] * k 
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.size+1) <= self.capacity:
            
            self.circular_q[self.rear] = value
            self.rear = ( self.rear +  1 ) % self.capacity
            self.size += 1 
            
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size != 0:
        
            self.front = ( self.front + 1) % self.capacity
            self.size -= 1
            
            return True
        else:
            return False
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size != 0:
            return self.circular_q[ self.front ]
        else:
            return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size != 0:
            return self.circular_q[ (self.rear-1) % self.capacity ]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity        



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