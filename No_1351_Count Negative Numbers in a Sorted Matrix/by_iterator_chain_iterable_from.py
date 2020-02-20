'''

Description:

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

'''


from typing import List
from itertools import chain
class Solution:
        
    
    def countNegatives(self, grid: List[List[int]]) -> int:
                
        return sum( 1 for element in chain.from_iterable( grid ) if element < 0 )



# m : the dimension of column in matrix
# n : the dimension of row in matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the iteration length of generator expresionn, which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for generator, which is of O( 1 )



def test_bench():

    test_data = [
                    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
                    [[3,2],[1,0]],
                    [[1,-1],[-1,-1]],
                    [[-1]]
                ]

    # expected output:
    '''
    8
    0
    3
    1
    '''


    for matrix in test_data:

        print( Solution().countNegatives(matrix) )
    
    return



if __name__ == '__main__':

    test_bench()