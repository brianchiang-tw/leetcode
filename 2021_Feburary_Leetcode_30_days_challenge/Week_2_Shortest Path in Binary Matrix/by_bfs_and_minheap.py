'''

Description:

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2



Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4



Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

'''

from heapq import heappush, heappop
from itertools import product

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        
        # n = size - 1
        n = len(grid)-1
        
        
        if grid[0][0] or grid[n][n]: 
            
            # Quick rejection when source or destination has obstacle
            return -1
        
        # direction vector
        directions = [x for x in product((-1, 0, 1), repeat=2) if x != (0,0)]
        
        # traversal queue,
        # parameter: evaluation, current step, current i, current j
        q = [(n + 1, 1, n, n)] 
        
        grid[n][n] = -1 # the step of the start is 1 
        
        # go from destination to source
        while q:
            
            # pop one grid with minimal evaluation value
            _, step, i, j = heappop(q)
            
            
            if (i, j) == (0, 0): 
                
                # arrive the source, return minimal step
                return step          

            
            # explore each possible next move
            for di, dj in directions:
                
                newI, newJ = i+di, j+dj
                
                # Except grid[i][j] = 1, we need to search and update  
                if 0 <= newI <= n and 0 <= newJ <= n and grid[newI][newJ] < 1:
                    
                    newStep = step + 1
                    
                    # if we have new visit or can have fewer steps, update
                    if grid[newI][newJ] == 0 or grid[newI][newJ] < -newStep:
                        
                        # store new minimal step
                        grid[newI][newJ] = -newStep
                        
                        # compute evaluation based on coordination
                        evaluation = max(newI, newJ) + newStep
                        
                        # add current move to traversal queue
                        heappush(q, (evaluation, newStep, newI, newJ))
                        
        return -1


# m: the height of grid
# n: the width of grid


## Time Complexity: O( m*n )
#
# The overhead in time is the cost of BFS traversal with min-heap, which is of O( m*n )

## Space Complexity: O( m*n )
#
# The overhead in space is the cost of min-heap as traversal queue, which is of O( m*n )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().shortestPathBinaryMatrix( grid=[[0,1],[1,0]] )
        self.assertEqual(result, 2)

    
    def test_case_2( self ): 

        result = Solution().shortestPathBinaryMatrix( grid=[[0,0,0],[1,1,0],[1,1,0]] )
        self.assertEqual(result, 4)


if __name__ == '__main__':        

    unittest.main()