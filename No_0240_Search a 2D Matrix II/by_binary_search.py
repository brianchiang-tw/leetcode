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
            # Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        for row in matrix:
        
            if row[0] <= target <= row[-1]:
                
                left, right = 0, w-1
                
                while left <= right:
                    
                    mid = left + (right - left) // 2
                    
                    mid_value = row[mid]
                    
                    if target > mid_value:
                        left = mid+1
                    elif target < mid_value:
                        right = mid-1
                    else:
                        return True
                
        return False



# m : the dimension of row of input matrix
# n : the dimension of column of input matrix            

## Time Complexity: O( m log n )
#
# The overhead in time is the for loop, which is of O( m ), and
# the cost of binary search, which is of O( log n )
# It takes O( m log n ) in total.

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

            
            