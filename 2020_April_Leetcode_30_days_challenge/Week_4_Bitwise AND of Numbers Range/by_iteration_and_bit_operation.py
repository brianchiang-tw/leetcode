'''

Description:

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

'''


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        shift = 0

        # find common bits from LSB to MSB
        while m != n :

            m >>= 1
            n >>= 1

            shift += 1

        return ( m << shift )



# m, n : input number pair

## Time Complexity: O( 1 )
#
# Description has guarantees the upper bound of input, thus the time complexity is of O( 32 ) = O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bitwise operation



def test_bench():

    test_data = [
                    (5, 7),
                    (30, 63),
                    (2**20, 2**20+7)
                ]


    # expected output:
    '''
    4
    0
    1048576
    '''

    for m, n in test_data:
        print( Solution().rangeBitwiseAnd(m, n) )

    return 



if __name__ == '__main__':
    
    test_bench()