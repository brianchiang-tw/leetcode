'''

Description:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack=[]
        self._min = 2**32

    def push(self, x: int) -> None:
        self._stack.append( x)
        
        if x < self._min:
            self._min = x
        
    def pop(self) -> None:
        x = self._stack.pop()
        
        if x == self._min and len(self._stack) != 0:
            self._min = min( self._stack )
        elif len(self._stack) == 0:
            self._min = 2 ** 32

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        if len(self._stack) != 0:
            return self._min
        
        else:
            return None


# N : number of elements to push in

## Time Complexity : O( 1 )
#
# MinStack's push(), pop(), top(), getMin() is of O( 1 ), 
# getMin() is O(1) because we update and save global minimal on every push operation.

## Space Complexity : O( N )
#
# The major overhead is the space allocated to _stack[], its groth order is of O( N )
# The minor overhead is member varaible _min of O( 1 )


def test_bench():

    test_data = [6,3,5,2,1,4]


    # expected output:
    '''
    6
    2
    2
    5
    3
    4
    1
    '''


    min_stk = MinStack()

    min_stk.push( test_data.pop(0) )
    print( min_stk.getMin() )

    min_stk.push( test_data.pop(0) )
    min_stk.push( test_data.pop(0) )
    min_stk.push( test_data.pop(0) )
    print( min_stk.top() )
    print( min_stk.getMin() )

    min_stk.pop()
    print( min_stk.top() )
    print( min_stk.getMin() )


    min_stk.push( test_data.pop(0) )
    min_stk.push( test_data.pop(0) )
    print( min_stk.top() )
    print( min_stk.getMin() )



if __name__ == '__main__':

    test_bench()
