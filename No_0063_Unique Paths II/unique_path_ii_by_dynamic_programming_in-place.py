'''

Description:

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''


# Dynamic Programming relation of unique path:

# Base case:

# DP(0, 0) = 1, if grid[0][0] == 0 without obstable
# DP(0, 0) = 0, if grid[0][0] == 1 with obstable


# DP(0, j) = DP(0, j-1), if grid[0][j] == 0 without obstacle, 
# [0][j] is only reachable from one step left

# DP(0, j) = 0, if grid[0][j] == 1 with obstacle


# DP(i, 0) = DP(i-1, 0), if grid[i][0] == 0 without obstacle, 
# [i][0] is only reachable from one step up

# DP(i, 0) = 0, if grid[i][0] == 1 with obstacle



# General case:
# DP(i,j) = number of path reach to (i, j)
#         = number of path reach to one step left + number of path reach to one step up
#         = number of path reach to (i, j-1) + number of path to (i-1, j)
#         = DP(i, j-1) + DP(i-1, j)



from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        
        for m in range(num_rows):
            for n in range(num_cols):
                if obstacleGrid[m][n] == 1:
                    obstacleGrid[m][n] = -1
        
        if obstacleGrid[0][0] != -1:
            obstacleGrid[0][0] = 1
        
        total_ways = 0
        for m in range(num_rows):
            for n in range(num_cols):
                if obstacleGrid[m][n] != -1:
                    if m > 0 and obstacleGrid[m-1][n] != -1:
                        obstacleGrid[m][n] += obstacleGrid[m-1][n]
                    if n > 0 and obstacleGrid[m][n-1] != -1:
                        obstacleGrid[m][n] += obstacleGrid[m][n-1]
                else:
                    obstacleGrid[m][n] = 0
                
        return obstacleGrid[num_rows-1][num_cols-1]



# m,n : dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the nested for loops iterating on (i, j), which is of O( m * n )



## Space Complexity: O( m * n )
#
# The overhead in space is the table of dynamic programming, path_dp, which is of O( m * n )


def test_bench():

    test_data = [
                    [[0,0,0],
                    [0,1,0],
                    [0,0,0]],

                    [[0,1,0],
                    [0,1,0],
                    [0,0,0]],     

                    [[0,1,1],
                    [0,0,0],
                    [1,1,0]],                  
                ]

    # expected output:
    '''
    2
    1
    1    
    '''

    for maze in test_data:

        print( Solution().uniquePathsWithObstacles(maze) )
    
    return



if __name__ == '__main__':

    test_bench()