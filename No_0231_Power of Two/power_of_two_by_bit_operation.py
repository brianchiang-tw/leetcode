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
        
        chk_power_of_2 = n & ( n-1 )
        
        return chk_power_of_2 == 0


## Time Complexity: O( log n )
#
# The overhead in time is the bitwise and of n and n-1, which is of O( log n)

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for chk_power_of_2, which is of O( 1 )



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