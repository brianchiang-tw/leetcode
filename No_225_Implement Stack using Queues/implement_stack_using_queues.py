'''

Description:

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.buffer = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.inbox.append( x )
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len( self.inbox ) != 0:
            front_of_inbox = self.inbox.pop( 0 )
            
            if len( self.inbox ) != 0:
                self.buffer.append( front_of_inbox )
            else:
                top_element = front_of_inbox
                
        
        # swap inbox and buffer
        self.inbox, self.buffer = self.buffer, self.inbox
        
        return top_element

        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        while len( self.inbox ) != 0:
            front_of_inbox = self.inbox.pop( 0 )
            
            if len( self.inbox ) != 0:
                self.buffer.append( front_of_inbox )
            else:
                self.buffer.append( front_of_inbox )
                top_element = front_of_inbox
                
        
        # swap inbox and buffer
        self.inbox, self.buffer = self.buffer, self.inbox
        
        return top_element
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len( self.inbox ) + len( self.buffer ) == 0:
            return True
        
        else:
            return False


# N : the lenth of input elements

## Time Complexity: O( N )
#
# The overhead of push() is O( 1 )
# The overhead of top() is O( N )
# The overhead of pop() is O( N )
# The overhead of empty() is O( 1 )

## Space Complexity: O( N )
#
# The overhead in space is to maintain two queues: one is inbox, the other is buffer
# The length of inbox and buffer is at most O( N )


def test_bench():

    # expected output:
    '''
    2
    2
    False
    '''

    _stack = MyStack()

    _stack.push(1)

    _stack.push(2)

    print( _stack.top() )

    print( _stack.pop() )

    print( _stack.empty() )

    return



if __name__ == '__main__':

    test_bench()