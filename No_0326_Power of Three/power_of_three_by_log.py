'''

Description:

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true



Example 2:

Input: 0
Output: false



Example 3:

Input: 9
Output: true



Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

'''



from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0: 
            return False
        else:
            exponent = log( n, 3)
            return abs(exponent- round(exponent) ) < 1e-12



# n : the input value

## Time Complexity: O( log n )
#
# The overhead in time is the cost of logarithm, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of temporarily variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().isPowerOfThress
        return

    def test_case_1( self ):

        result = self.solver( n = 27 )
        self.assertEqual(result, True)

    
    def test_case_2( self ):

        result = self.solver( n = 0 )
        self.assertEqual(result, False)


    def test_case_3( self ):

        result = self.solver( n = 9 )
        self.assertEqual(result, True)

    def test_case_4( self ):

        result = self.solver( n = 45 )
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()        