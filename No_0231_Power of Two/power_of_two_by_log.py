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

from math import log
from math import floor

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0 or n < 0:
            return False    
        
        log_2_n = log( n, 2.0 )
        
        return abs( floor(log_2_n) - log_2_n ) < 10e-15



## Time Complexity: O( log n )
#
# The overhead in time is log n in base 2, which is of O( log n)

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for log_2_n, which is of O( 1 )



def test_bench():

    test_data = [-2, 0, 1, 2, 3, 4, 7, 16, 2 **32 - 1, 2 ** 32 ]

    # expected output:
    '''
    False
    False
    True
    True
    False
    True
    False
    True
    False
    True
    '''


    for n in test_data:

        print( Solution().isPowerOfTwo(n) ) 

    return 



if __name__ == '__main__':

    test_bench() 