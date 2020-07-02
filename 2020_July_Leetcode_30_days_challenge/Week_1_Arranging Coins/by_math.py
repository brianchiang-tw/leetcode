'''

Description:

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''



from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:

        #quick response
        if n <= 1:
            return n
                
        #solve k(k+1)/2 <= n , keep k as large as possible
        k = int( (-1 + sqrt( 1 + 8*n )) / 2 )
        
        return k



# Time Complexity: O( 1 )
#
# The overhead in time is the cost of formula computation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().arrangeCoins( n = 5 )
        self.assertEqual( result, 2)


    def test_case_2( self ):        

        result = Solution().arrangeCoins( n = 8 )
        self.assertEqual( result, 3)


    def test_case_3( self ):        

        result = Solution().arrangeCoins( n = 11 )
        self.assertEqual( result, 4)


if __name__ == '__main__':

    unittest.main()