'''

Description:

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"



Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9

'''


from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        hour, minute = -1, -1
        
        for h1, h2, m1, m2 in permutations(A):
            
            cur_hour, cur_min = 10*h1 + h2, 10*m1 + m2

            if cur_hour >= 24 or cur_min >= 60:
                
                # skip invaid clock time
                continue
                
                
            if cur_hour * 60 + cur_min > hour*60 + minute:
                # update and record maximum clock time
                hour, minute = cur_hour, cur_min
                    
                    
        if (hour, minute) == (-1, -1):
            return ""
        
        else:
            # convert to clock string with zero-padding on the front
            clock_string = [f'{hour:02}', f'{minute:02}']
            return ':'.join( clock_string )



## Time Complexity: O( 4! ) = O( 24 ) = O( 1 )
#
# The overhead in time is the cost of permutation, which is of O( 1 )

## Space Complexity: O( 1 ):
#
# The overhead in space is the storage for loop index and temporary variable, whichi is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().largestTimeFromDigits( A=[1,2,3,4] )
        self.assertEqual(result, '23:41')


    def test_case_2( self ):

        result = Solution().largestTimeFromDigits( A=[0,1,2,3] )
        self.assertEqual(result, '23:10')


    def test_case_3( self ):

        result = Solution().largestTimeFromDigits( A=[5,5,5,5] )
        self.assertEqual(result, '')



if __name__ == '__main__':

    unittest.main()