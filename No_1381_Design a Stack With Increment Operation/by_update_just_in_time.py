'''

Description:

Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
 

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.
 

Constraints:

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.

'''



class Entry:
    def __init__(self, value, offset ):
        
        self.value = value
        self.offset = offset

        
    def __repr__(self):
        # override __repr__ to help programmer trace and debug
        msg = [ f'value = {self.value}', f'offset = {self.offset}', '---']
        return '\n'.join( msg )
    

    def __str__(self):
        return self.__repr__()
        
        
class CustomStack:

    def __init__(self, maxSize: int):
        
        self.stk = []
        self.size_limit = maxSize

        
        
    def push(self, x: int) -> None:

        
        if len(self.stk) < self.size_limit:
            
            # push new element when stack size is within limit
            self.stk.append( Entry( value = x, offset = 0) )


        
    def pop(self) -> int:
        
        if self.stk:
            
            # fetch and pop top element from stack
            top_element = self.stk.pop()
            
            if self.stk:
                # If stack is still non-empty, 
                # propagate increment offset to lower level
                self.stk[-1].offset += top_element.offset
            

            # compute result with increment offset
            return top_element.value + top_element.offset
        
        else:
            
            # stack is empty, directly return -1
            return -1

        
        
    def increment(self, k: int, val: int) -> None:
        

        if self.stk:
            
            # update offset at k-th element when stack is non-empty
            
            # adjust k if k is over stack size
            k = min( k, len(self.stk) )
            
            self.stk[k-1].offset += val


    def __str__(self):
        # __str__ is override to help programmer trace and debug
        return '\n'.join( str(entry) for entry in self.stk )



# Time Compleixty: amortized O( 1 )  for __init__(), push(), pop(), increment()

# Space Complexity: amortized O( 1 ) for __init__(), push(), pop(), increment()




def test_bench():


    # Please follow those print message and comment to trace the example

    customStack = CustomStack(3)                   # Stack is Empty []

    print( customStack )
    print( '\n-------------------------------\n')
    customStack.push(1)                            # stack becomes [1]

    print( customStack )
    print( '\n-------------------------------\n')

    customStack.push(2)                            # stack becomes [1, 2]

    print( customStack )
    print( '\n-------------------------------\n')

    customStack.pop()                              # return 2 --> Return top of the stack 2, stack becomes [1]

    print( customStack )
    print( '\n-------------------------------\n')

    customStack.push(2)                            # stack becomes [1, 2]

    print( customStack )
    print( '\n-------------------------------\n')

    customStack.push(3)                            # stack becomes [1, 2, 3]

    print( customStack )
    print( '\n-------------------------------\n')

    customStack.push(4)                            # stack still [1, 2, 3], Don't add another elements as size is 4
    
    print( customStack )
    print( '\n-------------------------------\n')
    
    customStack.increment(5, 100)                  # stack becomes [101, 102, 103]
    
    print( customStack )
    print( '\n-------------------------------\n')
    
    customStack.increment(2, 100)                  # stack becomes [201, 202, 103]
    
    print( customStack )
    print( '\n-------------------------------\n')
    
    customStack.pop()                              # return 103 --> Return top of the stack 103, stack becomes [201, 202]
    
    print( customStack )
    print( '\n-------------------------------\n')
    customStack.pop()                              # return 202 --> Return top of the stack 102, stack becomes [201]
    
    print( customStack )
    print( '\n-------------------------------\n')

    customStack.pop()                              # return 201 --> Return top of the stack 101, stack becomes []
    
    print( customStack )
    print( '\n-------------------------------\n')
    
    customStack.pop()                              # return -1 --> Stack is empty return -1.

    print( customStack )
    print( '\n-------------------------------\n')


if __name__ == '__main__':

    test_bench()