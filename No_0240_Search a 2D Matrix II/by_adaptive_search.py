'''

Description:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

'''


from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:

        
        if not len(matrix) or not len(matrix[0]):
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        # Start adaptive search from bottom left corner
        y, x = h-1, 0
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target < current:
                # target is smaller, then go up
                y -= 1
            
            elif target > current:
                # target is larger, then go right
                x += 1
            
            else:
                # hit target
                return True
            
        return False



# m : the dimension of row of input matrix
# n : the dimension of column of input matrix            

## Time Complexity: O( m + n )
#
# The overhead in time is the maximum finding path, which is of O( m + n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for coordination, which is of O( 1 )


def test_bench():
    
    matrix =    [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
                ]

    test_data = [ 5, 20, 11]

    #expected output:
    '''
    True
    False
    True
    '''

    for t in test_data:

        print( Solution().searchMatrix( matrix = matrix, target = t ) )

    return



if __name__ == '__main__':

    test_bench()

            
            