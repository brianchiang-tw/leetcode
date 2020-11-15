'''

Description:

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]



Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1

'''



from typing import List
from unittest import result

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        h, w = len(A), len(A[0])
        
        for y in range(h):
            
            
            for x in range(w//2):
                
                # flip the image horizontally
                A[y][x], A[y][w-1-x] = A[y][w-1-x], A[y][x]
            
            for x in range(w):
                
                # invert image by toggle with 1
                A[y][x] ^= 1
                
                
        return A
                
            
# m : the height of input image A
# n : the width of input image A

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested for-loops, which is of O( m*n )

## Space Complexity: O( 1 )
#
# The overhead in space is the stoarge for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().flipAndInvertImage( A=[[1,1,0],[1,0,1],[0,0,0]] )
        self.assertEqual(result, [[1,0,0],[0,1,0],[1,1,1]] )


    def test_case_2( self ):
        result = Solution().flipAndInvertImage( A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] )
        self.assertEqual(result, [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] )        


if __name__ == '__main__':

    unittest.main()        