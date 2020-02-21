'''

Description:

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.



Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]



Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''


from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        h, w = len( matrix), len( matrix[0])
        
        row_mask, col_mask = 0, 0
        
        ## Step_#1
        #
        # Setup masking for zero element
        for y in range(h):
            for x in range(w):
                
                if matrix[y][x] == 0:
                    
                    row_mask |= (1<<y)
                    col_mask |= (1<<x)
        
        
        ## Step_#2
        #
        # Clear by row mask and column mask
        for y in range(h):
            for x in range(w):
                
                if row_mask & (1<<y) or col_mask & (1<<x):
                    matrix[y][x] = 0



# m : the dimension of column of matrix
# n : the dimension of row of matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loops, which is of O( m*n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bitmasking, 
# row_mask as well as col_mask, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'matrix')

def print_matrix( mat ):

    h, w = len(mat), len(mat[0])

    for y in range(h):
      for x in range(w):
        print(f'{mat[y][x]:3}', end = ' ')
      
      print()
    
    print()
    return




def test_bench():

    test_data = [
                  TestEntry([
                              [1,1,1],
                              [1,0,1],
                              [1,1,1]
                            ]),

                  TestEntry([
                              [0,1,2,0],
                              [3,4,5,2],
                              [1,3,1,5]
                            ])
                ]

    # expected output:
    '''
    1   0   1
    0   0   0
    1   0   1

    0   0   0   0
    0   4   5   0
    0   3   1   0

    '''



    instance = Solution()
    for t in test_data:
      instance.setZeroes(t.matrix)
      print_matrix( t.matrix )

    return 



if __name__ == '__main__':

  test_bench()