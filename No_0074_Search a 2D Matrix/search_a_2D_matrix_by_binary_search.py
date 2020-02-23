'''

Description:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

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



# m : the dimension of matrix column.
# n : the dimension of matrix row

## Time Compleity: O( log m + log n )
#
# The overhead in time is the cost of two 1D binary search, 
# which is of O( log m ) + O( log n ) = O( log m + log n).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for index variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'matrix target')

def test_bench():

    test_data = [
                    TestEntry(  matrix =    [
                                                [1,   3,  5,  7],
                                                [10, 11, 16, 20],
                                                [23, 30, 34, 50]
                                            ], 
                                target = 3),

                    TestEntry( matrix =     [
                                                [1,   3,  5,  7],
                                                [10, 11, 16, 20],
                                                [23, 30, 34, 50]
                                            ], 
                                target = 13 )
                ]

    # expected output:
    '''
    True
    False
    '''

    for t in test_data:
        print( Solution().searchMatrix( matrix = t.matrix, target= t.target ) )

    return


if __name__ == '__main__':

    test_bench()