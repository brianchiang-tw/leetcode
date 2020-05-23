'''

Description:

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4



Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.



Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

'''


from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Constant for grid state
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        
        # Get dimension of grid
        h, w = len(grid), len(grid[0])
        
        # record for fresh oranges
        fresh_count = 0
        
        # record for position of initial rotten oranges
        rotten_grid = []        
        
        for y in range(h):
            for x in range(w):
                
                if grid[y][x] == FRESH :
                    fresh_count += 1
                    
                elif grid[y][x] == ROTTEN:
                    rotten_grid.append( (y, x, 0) )
        
        
        if fresh_count == 0:
            # Quick response for no fresh organe
            return 0
        
        
        traversal_queue = deque( rotten_grid )
        
        # Launch BFS from rotten grid
        while traversal_queue:
            
            cur_y, cur_x, time_stamp = traversal_queue.popleft()
            
            if 0 <= cur_y < h and 0 <= cur_x < w and grid[cur_y][cur_x] in (FRESH, ROTTEN):
                
                if grid[cur_y][cur_x] == FRESH:
                    
                    # This orange is rotten on current iteration
                    # update fresh count
                    fresh_count -= 1

                    # Mark as visited with time stamp
                    grid[cur_y][cur_x] = -time_stamp
				 
					# update minute
                    minute = time_stamp
            
                if ( grid[cur_y][cur_x] < 0 ) or ( time_stamp == 0 ):
                    
                    # BFS with new time stamp
                    traversal_queue.append( (cur_y-1, cur_x, time_stamp+1) )
                    traversal_queue.append( (cur_y+1, cur_x, time_stamp+1) )
                    traversal_queue.append( (cur_y, cur_x-1, time_stamp+1) )
                    traversal_queue.append( (cur_y, cur_x+1, time_stamp+1) )
                
        # ----------------------------------------------------------------
        
        if fresh_count == 0:
            # All orange is rotten finally
            return minute
        else:
            # Some orange still keep fresh
            return -1
        


# m : the height of grid
# n : the width of grid

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of BFS traversal, which is of O( m*n )

## Space Complexity: O( m*n )
#
# The overhead in space is the storage for traversal queue, which is of O( m*n )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'grid')

def test_bench():

    test_data = [
                        TestEntry( grid = [[2,1,1],[1,1,0],[0,1,1]] ),
                        TestEntry( grid = [[2,1,1],[0,1,1],[1,0,1]] ),
                        TestEntry( grid = [[0,2]] ),
                        TestEntry( grid = [[1,2,2]] ),
                        TestEntry( grid = [[1,1,1,1],[2,1,1,2],[1,1,1,1]] ),
                ]

    # expected output:
    '''
    4
    -1
    0
    1
    2
    '''

    for t in test_data:

        print( Solution().orangesRotting( grid = t.grid ) )
    
    return




if __name__ == '__main__':

    test_bench()    

