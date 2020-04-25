'''

Description:

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

'''

class BinaryMatrix:

    def __init__(self, matrix ):
        self._matrix = matrix

    def dimensions(self):
        # return [ row of matrix, col of matrix ]
        return [ len(self._matrix), len(self._matrix[0]) ]

    def get(self, row, col):
        return self._matrix[row][col]



class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        # get dimension of 2D array
        h, w = binaryMatrix.dimensions()
        
        y = 0
        left_most_column = w
        left, right = 0, w
        
        # Search from top to down
        # For each row, carry out binary search to find the leftmost column with 1
        while y < h:
            
            left = 0
            
            while left < right:
                
                mid = left + (right-left) // 2
                
                if binaryMatrix.get(y,mid) == 1:
                    # update right boundary of the column with 1
                    right = mid
                else:
                    left = mid+1
            
            # update left-most column who has 1
            left_most_column = left
            
            # move to next row
            y += 1
        
        
        if left_most_column == w:
            return -1
        else:
            return left_most_column




# n : the row dimension of matrix
# m : the column dimension of matrix

## Time Complexity: O( n log m )
#
# The overhead in time is the cost of row-wise binary search.
# The outer row-wise scan takes O( n ).
# The inner columns-wise binary search takes O( log m ).
# It takes O( n log m ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of loop index and temporary variable, which is of O( 1 )




def test_bench():

    test_data = [
                    BinaryMatrix( matrix = [[0,0],
                                            [1,1]] ),

                    BinaryMatrix( matrix = [[0,0],
                                            [0,1]] ),

                    BinaryMatrix( matrix = [[0,0],
                                            [0,0]] ),

                    BinaryMatrix( matrix = [[0,0,0,1],
                                            [0,0,1,1],
                                            [0,1,1,1]] ),
                ]

    # expected output:
    '''
    0
    1
    -1
    1
    '''


    for t in test_data:

        print( Solution().leftMostColumnWithOne( binaryMatrix = t) )
    
    return



if __name__ == '__main__':

    test_bench()