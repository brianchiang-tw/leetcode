'''

Description:

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

 

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
 

Note:

1 <= X <= 10^9
1 <= Y <= 10^9

'''



class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        
        if X >= Y:
            # Base case, also known as stop condition
            return X-Y
        
        else:
            
            if Y%2 == 1:
                # Y is odd
                return 1 + self.brokenCalc( X, Y+1 )
            else:
                # Y is even
                return 1 + self.brokenCalc( X, Y // 2)


# X, Y: the input value of paramter

## Time Complexity: O( log(y/x) )
#
# The overhead in time is the deepest recursion call depth, which is of O( log(y/x) )

## Space Complexity: O( log(y/x) )
#
# The overhead in space is the storage for recurison call stack, which is of O( log(y/x) )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'X Y')
def test_bench():

    test_data = [
                    TestEntry( X = 2, Y = 3 ),
                    TestEntry( X = 5, Y = 8 ),
                    TestEntry( X = 3, Y = 10 ),
                    TestEntry( X = 1024, Y = 1 ),
                ]

    # expected output:
    '''
    2
    2
    3
    1023
    '''

    for t in test_data:
        print( Solution().brokenCalc( X = t.X, Y = t.Y ) )   

    return



if __name__ == '__main__':

    test_bench()