'''

Description:

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

'''


from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        h, w = len(grid), len(grid[0])
        
        if h * w == 0:
            # Quick response for simple case
            return 0
        
        land_cell, internal_edge = 0, 0
        
		# scan each cell from top to bottom, from left to right
        for y in range(h):
            for x in range(w):
                
                if grid[y][x] == 1:
					# current cell is land
                    land_cell += 1
        
                    if y and grid[y-1][x]:
						# current land cell share one internal edge with neighbor land cell on the top
                        internal_edge += 1
                    
                    if x and grid[y][x-1]:
						# current land cell share one internal edge with neighbor land cell of the left
                        internal_edge += 1
                        
						
        # each land cell contributes 4 edge
        # each internal edge is repeatedly counted by 2 adjacent land cells
        perimeter = land_cell * 4 - internal_edge * 2
        
        return perimeter



# m, n: the dimension of height as well as weight of grid

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of nested loop, which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary viariable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().islandPerimeter( grid = [[0,1,0,0],[1,1,1,0], [0,1,0,0], [1,1,0,0]] )
        self.assertEqual( result, 16)
    


    def test_case_2( self ):
    
        result = Solution().islandPerimeter( grid = [[0,1,0],[1,1,1], [0,1,0]] )
        self.assertEqual( result, 12)
    


if __name__ == '__main__':

    unittest.main()