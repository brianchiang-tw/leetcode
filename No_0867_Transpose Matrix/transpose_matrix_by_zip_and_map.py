'''

Description:

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000

'''


# Note: 
#
# zip( *A ) = make tuple with ( A[0], A[1], A[2], ... ) from head to tail
#           = make tuple with ( row_0, row_1, row_2, ... ) from head to tail
#           = tuple of A transpose

# then use map with list over zip( *A) to make 2D array

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        a_transpose = list( map(list, zip(*A) ) )
        
        return a_transpose
