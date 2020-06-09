'''

Description:

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1



Example 2:

Input: 16
Output: true
Explanation: 24 = 16



Example 3:

Input: 218
Output: false

'''



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False    
        
        # note:
        # power of 2 in binary         = b' 1000 ... 0
        # power of 2 minus 1 in binary = b' 0111 ... 1
        # bitwise AND of n and (n-1) must be 0 if n is power of 2
        
        return ( n & ( n-1 ) ) == 0



# n : the value of Input

## Time Complexity: O( log n )
#
# The overhead in time is the cost of bitwise operation, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n')

def test_bench():

    test_data = [
                    TestEntry( n = -1 ),    # False
                    TestEntry( n = -2 ),    # False
                    TestEntry( n = 0 ),     # False
                    TestEntry( n = 1 ),     # True
                    TestEntry( n = 2 ),     # True
                    TestEntry( n = 3 ),     # False
                    TestEntry( n = 4 ),     # True
                    TestEntry( n = 218 ),   # False
                    TestEntry( n = 256 ),   # True
                    TestEntry( n = 1024 ),  # True
                    TestEntry( n = 1025 ),  # False
                ]
    
    for t in test_data:

        print( Solution().isPowerOfTwo(t.n))

    return



if __name__ == '__main__':

    test_bench()