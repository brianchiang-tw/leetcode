'''

Description:

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]



Example 2:

Input: rowIndex = 0
Output: [1]



Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 40

'''


from typing import List
from math import factorial

class Solution:
    
    def comb(self, n, m):
        
        if n == m or m == 0:
            return 1
        else:
            return factorial(n) // ( factorial(m) * factorial(n-m) )

        
    def getRow(self, rowIndex: int) -> List[int]:
        
        # the coefficient of level k is as following
        #
        # C(k,0), C(k,1), ... , C(k,k)
        
        return [ self.comb(rowIndex,i) for i in range(0, rowIndex+1) ]



# n : the number of input, rowIndex.

## Time Complexity: O( n )
#
# Assume the cost of factorial is O( 1 )
# The overhead in time is the cost of list comprehension, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storagre for output list, which is of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().getRow( 3 )
        self.assertEqual(result, [1, 3, 3, 1])
    

    def test_case_2( self ):
        
        result = Solution().getRow( 0 )
        self.aseertEqual(result, [1] )


    def test_case_3( self ):

        result = Solution().getRow( 1 )
        self.assertEqual(result, [1, 1] )