'''

Description:

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbox.append( x )
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        self.peek()
        return self.outbox.pop()
        
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        
        if len( self.outbox ) != 0:
            return self.outbox[-1]
        
        else:
            
            while len(self.inbox) != 0:
                
                top_of_inbox = self.inbox.pop()
                self.outbox.append( top_of_inbox )
        
            return self.outbox[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        if len(self.inbox) + len(self.outbox) == 0:
            return True
        else:
            return False
        


# N : the length of input element

## Time Complexity: O( N )
#
# The overhead of push is O( 1 )
# The overhead of peek and pop is O( N )
# The overhead of empty is O( 1 )

## Space Complexity: O( N )
#
# The overhead in space is to maintain two stacks: one is inbox , the other is outbox.
# The length of inbox and outbox is at most O( N )


def test_bench():


    # expected output:
    '''
    1
    1
    False
    '''

    _queue = MyQueue()

    _queue.push(1)

    _queue.push(2)

    print( _queue.peek() )

    print( _queue.pop() )

    print( _queue.empty() )


    return



if __name__ == '__main__':

    test_bench()
