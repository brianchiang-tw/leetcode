'''

Description:

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

 

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100

'''



from typing import List
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        size = len(A)
        
        if size == 1:
            # Quick response for single row
            return A[0][0]
        

        # Update A[y][x] from second row to last row
        for y in range( 1, size):
		
			# sacn each column from 0 to size-1
            for x in range( size ):
                
				# find falling path of minimal cost with optimal substructure
                min_prev = A[y-1][x] 
                
                if x > 0:
                    min_prev = min( min_prev, A[y-1][x-1] )
                
                if x < size-1:
                    min_prev = min( min_prev, A[y-1][x+1] )
                
                # update the cost of falling path, destination is [y][x], with optimal substructure
                A[y][x] = A[y][x] + min_prev
                
        
        # the cost of minimum falling path is the minimum value of last row
        return min( A[size-1] )



# n : the side length of square matrix

## Time Complexity: O( n^2 )
#
# The overhead in time is the nested for loops, which is of O( n^2 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and temporary variable for cost update, which are of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'square_matrix')

def test_bench():

    test_data = [
                    TestEntry( square_matrix = [[1,2,3],[4,5,6],[7,8,9]] ),
                    TestEntry( square_matrix = [[20,35],[28,16]] ),
                    TestEntry( square_matrix = [[25]] ),
                ]


    # expected output:
    '''
    12
    36
    25
    '''

    for t in test_data:
        print( Solution().minFallingPathSum( A = t.square_matrix) )



    return



if __name__ == '__main__':

    test_bench()