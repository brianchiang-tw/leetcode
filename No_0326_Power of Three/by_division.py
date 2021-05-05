'''

Description:

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true



Example 2:

Input: n = 0
Output: false



Example 3:

Input: n = 9
Output: true



Example 4:

Input: n = 45
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

'''



class Solution:

    def isPowerOfThress(self, n: int)-> bool:

        while n > 1:

            if n % 3 != 0:

                # Early rejection to those number which is not multiple of 3
                return False
            
            else:

                # keep dividing 3 if n is multiple of 3
                n //= 3

        # check if n is power of 3
        return n == 1


# n : the value in of input n

## Time Complexity: O( log n )
#
# The overhead in time is the cost of iteration of division, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of loop index and temporary variable, which is of O( 1 )

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