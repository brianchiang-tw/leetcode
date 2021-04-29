'''

Description:

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]



Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Example 3:

Input: matrix = [[1]]
Output: [[1]]



Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
		# reverse matrix upside down
		# select element from bottom to top
        matrix[:] = [ [ row[i] for row in reversed(matrix)] for i in range(len(matrix)) ]


# n : the height of square matrix

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of nested itertion, which is of O( n^2 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().rotate
        return

    def test_case_1( self ):
        
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.solver( matrix )
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])


    def test_case_2( self ):

        matrix = matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        self.solver( matrix )
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])


    def test_case_3( self ):

        matrix = [[1]]
        self.solver( matrix )
        self.assertEqual(matrix, [[1]])


    def test_case_4( self ):

        matrix =  [[1,2],[3,4]]
        self.solver( matrix )
        self.assertEqual(matrix,  [[3,1],[4,2]])



if __name__ == '__main__':

    unittest.main()        