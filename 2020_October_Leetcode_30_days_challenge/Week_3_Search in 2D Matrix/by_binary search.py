'''

Description:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true



Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false



Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

'''


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            # Reject invalid input, empty 1D list
            return False
        
        # Get height and width from input matrix
        h, w = len(matrix), len(matrix[0])
        
        if h * w == 0:
            # Reject invalid input, empty 2D list
            return False
        
        
        ## Step_#1
        # Binary seach on head elements of each row
        lower, upper = 0, h-1
        while lower <= upper:
            
            mid = lower + (upper-lower)//2
            
            mid_row_head_value = matrix[mid][0]
            
            if mid_row_head_value > target:
                upper = mid-1
            elif mid_row_head_value < target:
                lower = mid+1
            else:
                return True

            
        ## Step_#2
        # Binary seach on possible row
        row_idx = upper
        lower, upper = 0, w-1
        
        while lower <= upper:
            
            mid = lower + (upper-lower)//2
            
            mid_value = matrix[row_idx][mid]
            
            if mid_value > target:
                upper = mid-1
            elif mid_value < target:
                lower = mid+1
            else:
                return True
            
        return False


# m : the height of matrix
# n : the width of matrix

## Time Complexity: O( log m + log n )
#
# The overhead in time is the cost of binary search, which is of O( log m + log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().searchMatrix( matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]], target=3)
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().searchMatrix( matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]], target=13)
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()        