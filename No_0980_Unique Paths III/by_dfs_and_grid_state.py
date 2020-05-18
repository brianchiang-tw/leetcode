'''

Description:


On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)



Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)



Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

'''



# Define grid state to make it more readable

from collections import namedtuple
GridState = namedtuple('GridState', 'start ending empty obstacle')
grid_state = GridState( start = 1, ending = 2, empty = 0, obstacle = -1)


class Solution:
    def uniquePathsIII(self, grid):
            
        h, w = len( grid ), len( grid[0] )  
        
        available_grid_count = 0
        obstacle_count = 0
        
        src_row, src_col = 0, 0 
        
        self.valid_path_count = 0
        
        for y in range(h) :
            for x in range(w):
                
                if grid[y][x] == grid_state.obstacle:
                    obstacle_count += 1
                    
                elif grid[y][x] == grid_state.start:
                    src_row, src_col = y, x
        
        available_grid_count = h * w - obstacle_count
        
        # ------------------------------------------------------
        

        def dfs( cur_row, cur_col, depth):

            if grid[cur_row][cur_col] == grid_state.obstacle:

                # Terminate DFS when we are out of boundary or bumping into an obstacle
                return
            
            elif grid[cur_row][cur_col] == grid_state.ending:

                if depth == available_grid_count:
                    
                    # If we reach end with visiting all available grids, update valid path count
                    self.valid_path_count += 1
                
                # Terminate DFS when reach ending
                return
            
            else:
                
                state_backup = grid[cur_row][cur_col]
                # mark current grid as obstacle to avoid repeated visit
                grid[cur_row][cur_col] = grid_state.obstacle
                
                # DFS with valid index in range
                if cur_row-1 >= 0:
                    dfs( cur_row-1, cur_col, depth + 1)
                
                if cur_row+1 < h:
                    dfs( cur_row+1, cur_col, depth + 1)
                
                if cur_col-1 >= 0:
                    dfs( cur_row, cur_col-1, depth + 1)
                
                if cur_col+1 < w:
                    dfs( cur_row, cur_col+1, depth + 1)
                
                # restore original grid state
                grid[cur_row][cur_col] = state_backup
                
                return
            
        # ------------------------------------------------------
        
        dfs(src_row, src_col, depth = 1)
        return self.valid_path_count



# m : the dimension of rows
# n : the dimension of columns

## Time Compleity: O( 4^(mn) )
#
# The overhead in time is the execution tree of DFS, which is of O( 4^(mn) ).
# The base 4 comes from the number of all possible directions of next moves.

## Space Complexity: O( m*n )
#
# The overhead in space is the depth of recursion call stack, which is of O( m*n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'grid')

def test_bench():

    test_data = [
                    TestEntry( grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]] ),
                    TestEntry( grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]] ),
                    TestEntry( grid = [[0,1],[2,0]] ),
                ]

    # expected output:
    '''
    2
    4
    0
    '''

    for t in test_data:
        print( Solution().uniquePathsIII( grid = t.grid) )
        
    return



if __name__ == '__main__':

    test_bench()