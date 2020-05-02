'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
'''



from collections import namedtuple
Entry = namedtuple('Entry', 'element min_val')

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
        

    def push(self, x: int) -> None:
        
        cur_min = min( x, self.stack[-1].min_val ) if self.stack else x

        self.stack.append( Entry(x, cur_min) )

            
            
    def pop(self) -> None:
        
        self.stack.pop()
        
        

    def top(self) -> int:
        
        return self.stack[-1].element

    
    
    def getMin(self) -> int:
        
        return self.stack[-1].min_val



# N : number of elements to push in

## Time Complexity : O( 1 )
#
# MinStack's push(), pop(), top(), getMin() is of O( 1 ), 
# getMin() is O(1) because we update and save global minimal on every push operation.

## Space Complexity : O( N )
#
# The overhead is the space allocated to _stack[], its groth order is of O( N )


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
