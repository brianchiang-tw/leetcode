'''

The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1



Example 2:

Input: n = 1
Output: [0,1]

'''


from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        # total 2^n codes for bit length n
        code_count = 1 << n
        
        # generate gray code from 0, and toggle 1 bit on each iteration
        # toggle mask: ( i >> 1 )
        
        gray_codes =[ i ^ ( i >> 1 ) for i in range(code_count) ]
        
        return gray_codes


# n : the value of input n

## Time Complexity: O( n )
#
# The overhead in time is the cost of list comprehension, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().grayCode( n=2 )
        self.assertEqual(result, [0, 1, 3, 2])


    def test_case_2( self ):

        result = Solution().grayCode( n=1 )
        self.assertEqual(result, [0, 1])


if __name__ == '__main__':

    unittest.main()