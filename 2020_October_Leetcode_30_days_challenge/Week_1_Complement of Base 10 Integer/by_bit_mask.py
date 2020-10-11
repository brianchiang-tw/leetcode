'''

Description:

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.



Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.



Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9
This question is the same as 476: https://leetcode.com/problems/number-complement/

'''



class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        bit_length = N.bit_length()
        
        return N ^ (2 ** bit_length - 1) if N else 1



# n : the value of N

## Time Complexity: O( log n )
#
# The overhead in time is the cost of bitwise operation, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for bitmask, which is of O( log n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().bitwiseComplement( N=5 )
        self.assertEqual(result, 2)


    def test_case_2( self ):

        result = Solution().bitwiseComplement( N=7 )
        self.assertEqual(result, 0)


    def test_case_3( self ):

        result = Solution().bitwiseComplement( N=10 )
        self.assertEqual(result, 5)


    def test_case_4( self ):

        result = Solution().bitwiseComplement( N=0 )
        self.assertEqual(result, 1)

if __name__ == '__main__':

    unittest.main()