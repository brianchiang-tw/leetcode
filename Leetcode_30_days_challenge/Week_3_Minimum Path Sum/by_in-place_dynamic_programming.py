'''

Description:

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''



from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        h, w = len(grid), len(grid[0])
        
        # first column
        for y in range(1, h):
            grid[y][0] = grid[y-1][0] + grid[y][0]

        # first row            
        for x in range(1, w):
            grid[0][x] = grid[0][x-1] + grid[0][x]

        # general case            
        for y in range(1, h):
            for x in range(1, w):
                grid[y][x] = min( grid[y-1][x], grid[y][x-1]) + grid[y][x]
        
                
        return grid[-1][-1]
            


# m : the dimension of column of grid
# n : the dimension of row of grid

## Time Complexity: O( m * n)
#
# The overhead in time is the nested loop interating on grid, which is of O( m * n ).

## Space Complexity: O( 1 )
#
# The update of dp_table is in-place, thus the cost of space is of O( 1 ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'cost_matrix')

def test_bench():

    test_data = [
                    TestEntry( cost_matrix = [
                                                [1,3,1],
                                                [1,5,1],
                                                [4,2,1]
                                            ]
                            ),
                    
                    TestEntry( cost_matrix = [
                                                [5,6],
                                                [7,4]
                                            ]
                            ),
                ]

    # expected output:
    '''
    7
    15
    '''

    for t in test_data:

        print( Solution().minPathSum( grid = t.cost_matrix ) )
    
    return



if __name__ == '__main__':

    test_bench()