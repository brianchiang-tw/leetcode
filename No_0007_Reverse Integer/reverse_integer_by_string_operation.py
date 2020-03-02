'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment 
which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''



class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            
            # Reverse positive integer
            rev_int = int( str(x)[::-1] )
            
            if rev_int > 2**31-1:
                return 0
            else:
                return rev_int
            
            
        elif x < 0:
            
            # Reverse negative interger
            rev_int = -1*int( str( abs(x) )[::-1] )
            
            if rev_int < -2**31:
                return 0
            else:
                return rev_int
            
        else:
            
            # x is zero
            return 0
    


# n : the value of input x

## Time Complexity: O( log n )
#
# The overhead in time is the length of bitstring, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for bitstring, which is of O( log n )


def test_bench():

    test_integers = [123, -123, 120, 2**31]

    # expected output:
    '''
    321
    -321
    21
    0
    '''



    for x in test_integers:

        ret_value = Solution().reverse( x )

        print( ret_value )

    return



if __name__ == "__main__":

    test_bench()