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


class Solution:
    def islandPerimeter(self, grid):
        area = 0
        for row in grid + list(map(list, zip(*grid))):
            for i1, i2 in zip([0] + row, row + [0]):
                area += int(i1 != i2)
        return area



# m, n : the dimension of colums and rows of input test array, grid.

## Time Complexity: O( ( m + n )^2 )
#
# The overhead in time is the nested loop iterating on (row, i1, i2), which is of O( ( m + n )^2 ).

## Space Comeplxity: O( m + n )
#
# The overhead in space is the storage for grid + list(map(list, zip(*grid))), which is of O( m + n ).




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
    