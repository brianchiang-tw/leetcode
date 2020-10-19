'''

Description:

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.



Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6

'''


from typing import List


from collections import Counter

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)
        
        ## dictionary
        # key: point
        # value: occurrence of point in A
        point_occ_A = Counter(A)
        
        ## dictionary
        # key: point
        # value: occurrence of point in B
        point_occ_B = Counter(B)
        
        
        ## check occurene of A[0] and B[0]
        for point in (A[0], B[0]):
            
            if all( point in pair for pair in zip(A, B) ):
                
                # we can meet the requirement by swap
                return n - max( point_occ_A[point], point_occ_B[point] )
        
        # no chance to meet the requirement
        return -1

# n : the length of A

## Time Complexity: O( n )
#
# The overhead in time is the cost for-loop and dictionary building, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().minDominoRotations( A=[2,1,2,4,2,2], B=[5,2,6,2,3,2] )
        self.assertEqual(result, 2)


    def test_case_2( self ):

        result = Solution().minDominoRotations( A=[3,5,1,2,3], B=[3,6,3,3,4] )
        self.assertEqual(result, -1)



if __name__ == '__main__':

    unittest.main()