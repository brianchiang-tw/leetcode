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

'''



from typing import List
class Solution:
    
    def perimeter_contribute(self, coordinate, grid):
        
        
        h, w = len(grid), len(grid[0])
        y, x = coordinate
        
        up, down, left, right = True, True, True, True

        # check those directions are doable or not
        if x == 0:
            left = False
            
        if x == w-1:
            right = False
            
        if y == 0:
            up = False
            
        if y == h-1:
            down = False
        
        
        count_of_neighbor = 0
        
        # check neighbor existence
        if left and grid[y][x-1] == 1 :
            count_of_neighbor += 1
            
        if right and grid[y][x+1] == 1:
            count_of_neighbor += 1
        
        if up and grid[y-1][x] == 1 :
            count_of_neighbor += 1
        
        if down and grid[y+1][x] == 1 :
            count_of_neighbor += 1
        
        return (4-count_of_neighbor)
            
        
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        h, w = len(grid), len(grid[0])
        
        # sum the perimeter of each land grid
        perimeter = sum( [ self.perimeter_contribute( (y,x), grid) for y in range(h) for x in range(w) if grid[y][x] == 1 ] )
        
        return perimeter



# m, n : the dimension of colums and rows of input test array, grid.

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loop iterating on (x, y), which is of O( m * n ).

## Space Comeplxity: O( m * n )
#
# The overhead in space is the storage for list comprehension iterating on (x, y), which is of O( m * n ).




def test_bench():

    test_data = [
                    [[0,1,0,0],
                    [1,1,1,0],
                    [0,1,0,0],
                    [1,1,0,0]]
                ]

    for test_arr in test_data :

        print( Solution().islandPerimeter(test_arr) )

    return 



if __name__ == '__main__':

    test_bench()
    