'''

Description:

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8



Example 2:

Input: a = 2, b = [1,0]
Output: 1024

'''



from functools import reduce
from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        
        if a % 1337 == 0:
            return 0
        
        else:
            # Euler theorem:
            #
            # ( a ^ phi(n) ) mod n = 1
            #  
            # => ( a ^ b ) mod n = ( a ^ ( b mod phi(n) ) ) mod n
            #
            #exponent = int( ''.join( map( str, b) ) )
            
            exponent = int( ''.join( map( str, b) ) )
            return pow( a, exponent % 1140, 1337 )



# B : the length of input list, b
# n : the value of expoenent % 1140

## Time Complexity: O( n )
#
# The overhead in time is the times of multiplication, which is of O( n ),
# and the extraction of exponent, which is of O( B )

## Space Complexity: O( 1 )
#
# THe overhead in space is the storage for power, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'a b')
def test_bench():

    test_data = [       
                    TestEntry( a = 2, b = [ 0 ] ),
                    TestEntry( a = 2, b = [ 1 ] ),
                    TestEntry( a = 2, b = [ 2 ] ),
                    TestEntry( a = 2, b = [ 1, 0 ] ),
                    TestEntry( a = 78267, b = [1,7,7,4,3,1,7,0,1,4,4,9,2,8,5,0,0,9,3,1,2,5,9,6,0,9,9,0,9,6,0,5,3,7,9,8,8,9,8,2,5,4,1,9,3,8,0,5,9,5,6,1,1,8,9,3,7,8,5,8,5,5,3,0,4,3,1,5,4,1,7,9,6,8,8,9,8,0,6,7,8,3,1,1,1,0,6,8,1,1,6,6,9,1,8,5,6,9,0,0,1,7,1,7,7,2,8,5,4,4,5,2,9,6,5,0,8,1,0,9,5,8,7,6,0,6,1,8,7,2,9,8,1,0,7,9,4,7,6,9,2,3,1,3,9,9,6,8,0,8,9,7,7,7,3,9,5,5,7,4,9,8,3,0,1,2,1,5,0,8,4,4,3,8,9,3,7,5,3,9,4,4,9,3,3,2,4,8,9,3,3,8,2,8,1,3,2,2,8,4,2,5,0,6,3,0,9,0,5,4,1,1,8,0,4,2,5,8,2,4,2,7,5,4,7,6,9,0,8,9,6,1,4,7,7,9,7,8,1,4,4,3,6,4,5,2,6,0,1,1,5,3,8,0,9,8,8,0,0,6,1,6,9,6,5,8,7,4,8,9,9,2,4,7,7,9,9,5,2,2,6,9,7,7,9,8,5,9,8,5,5,0,3,5,8,9,5,7,3,4,6,4,6,2,3,5,2,3,1,4,5,9,3,3,6,4,1,3,3,2,0,0,4,4,7,2,3,3,9,8,7,8,5,5,0,8,3,4,1,4,0,9,5,5,4,4,9,7,7,4,1,8,7,5,2,4,9,7,9,1,7,8,9,2,4,1,1,7,6,4,3,6,5,0,2,1,4,3,9,2,0,0,2,9,8,4,5,7,3,5,8,2,3,9,5,9,1,8,8,9,2,3,7,0,4,1,1,8,7,0,2,7,3,4,6,1,0,3,8,5,8,9,8,4,8,3,5,1,1,4,2,5,9,0,5,3,1,7,4,8,9,6,7,2,3,5,5,3,9,6,9,9,5,7,3,5,2,9,9,5,5,1,0,6,3,8,0,5,5,6,5,6,4,5,1,7,0,6,3,9,4,4,9,1,3,4,7,7,5,8,2,0,9,2,7,3,0,9,0,7,7,7,4,1,2,5,1,3,3,6,4,8,2,5,9,5,0,8,2,5,6,4,8,8,8,7,3,1,8,5,0,5,2,4,8,5,1,1,0,7,9,6,5,1,2,6,6,4,7,0,9,5,6,9,3,7,8,8,8,6,5,8,3,8,5,4,5,8,5,7,5,7,3,2,8,7,1,7,1,8,7,3,3,6,2,9,3,3,9,3,1,5,1,5,5,8,1,2,7,8,9,2,5,4,5,4,2,6,1,3,6,0,6,9,6,1,0,1,4,0,4,5,5,8,2,2,6,3,4,3,4,3,8,9,7,5,5,9,1,8,5,9,9,1,8,7,2,1,1,8,1,5,6,8,5,8,0,2,4,4,7,8,9,5,9,8,0,5,0,3,5,5,2,6,8,3,4,1,4,7,1,7,2,7,5,8,8,7,2,2,3,9,2,2,7,3,2,9,0,2,3,6,9,7,2,8,0,8,1,6,5,2,3,0,2,0,0,0,9,2,2,2,3,6,6,0,9,1,0,0,3,5,8,3,2,0,3,5,1,4,1,6,8,7,6,0,9,8,0,1,0,4,5,6,0,2,8,2,5,0,2,8,5,2,3,0,2,6,7,3,0,0,2,1,9,0,1,9,9,2,0,1,6,7,7,9,9,6,1,4,8,5,5,6,7,0,6,1,7,3,5,9,3,9,0,5,9,2,4,8,6,6,2,2,3,9,3,5,7,4,1,6,9,8,2,6,9,0,0,8,5,7,7,0,6,0,5,7,4,9,6,0,7,8,4,3,9,8,8,7,4,1,5,6,0,9,4,1,9,4,9,4,1,8,6,7,8,2,5,2,3,3,4,3,3,1,6,4,1,6,1,5,7,8,1,9,7,6,0,8,0,1,4,4,0,1,1,8,3,8,3,8,3,9,1,6,0,7,1,3,3,4,9,3,5,2,4,2,0,7,3,3,8,7,7,8,8,0,9,3,1,2,2,4,3,3,3,6,1,6,9,6,2,0,1,7,5,6,2,5,3,5,0,3,2,7,2,3,0,3,6,1,7,8,7,0,4,0,6,7,6,6,3,9,8,5,8,3,3,0,9,6,7,1,9,2,1,3,5,1,6,3,4,3,4,1,6,8,4,2,5] ),
                ]

    # expected output:
    '''
    1
    2
    4
    1024
    70
    '''



    for t in test_data:

        print( Solution().superPow( a = t.a, b = t.b ) )

    return 



if __name__ == '__main__':

    test_bench()