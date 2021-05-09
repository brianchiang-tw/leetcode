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




from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        allow_to_visit = lambda x, y: (1 - obstacleGrid[y][x] )
        
        # height and width of matrix
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        
        if h * w == 0 or not allow_to_visit(0, 0):
            
            # Quick response for invalid cases
            return 0
        
        
        # update [0][0] as start point with one valid path
        obstacleGrid[0][0] = 1
        
        ## base case: leftmost column
        for y in range(1, h):
            obstacleGrid[y][0] = obstacleGrid[y-1][0] * allow_to_visit(0, y)
        
        
        ## base case: top row
        for x in range(1, w):
            obstacleGrid[0][x] = obstacleGrid[0][x-1] * allow_to_visit(x, 0)
        
        
        ## general cases
        for y in range(1, h):
            for x in range(1, w):
                
                # update path count from left and top
                obstacleGrid[y][x] = (obstacleGrid[y][x-1] + obstacleGrid[y-1][x]) * allow_to_visit(x, y)
        
        return obstacleGrid[h-1][w-1]


# m,n : dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the nested for loops iterating on (i, j), which is of O( m * n )



## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary varaible, which is of O( 1 )


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