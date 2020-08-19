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
        
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        
        h, w = len(grid), len(grid[0])
        
        rotting_source = deque()
        fresh_count = 0
        t = 0
        for y in range(h):
            for x in range(w):
                
                if grid[y][x] == FRESH:
                    fresh_count += 1
                    
                elif grid[y][x] == ROTTEN:
                    rotting_source.append( (x, y, 0) )
                    
        # --------------------------------------------------------
        
        while rotting_source:
            
            x, y, time_stamp = rotting_source.popleft()
            
            for dx, dy in ( (+1, 0), (-1, 0), (0, +1), (0, -1) ):
                next_x, next_y = x + dx, y + dy
                
                if next_x < 0 or next_x == w or next_y < 0 or next_y == h or grid[next_y][next_x] != FRESH:
                    
                    # Out of boundary, or current orange is not in FRESH state
                    continue
            
            
                # update timer t and fresh count
                t = time_stamp + 1
                fresh_count -= 1
                
                # mark current orange as rotten
                grid[next_y][next_x] = ROTTEN
                rotting_source.append( (next_x, next_y, time_stamp+1) )
            
        # --------------------------------------------------------
            
        if fresh_count == 0:
            return t
        
        else:
            return -1


# m : the dimension of grid height
# n : the dimension of grid width

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of BFS, which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for traversal queue, which is of O( m * n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().orangesRotting( grid=[[2,1,1],[1,1,0],[0,1,1]] )
        self.assertEqual(result, 4)


    def test_case_2(self):

        result = Solution().orangesRotting( grid=[[2,1,1],[0,1,1],[1,0,1]] )
        self.assertEqual(result, -1)


    def test_case_3(self):

        result = Solution().orangesRotting( grid=[[0,2]] )
        self.assertEqual(result, 0)


    def test_case_4(self):

        result = Solution().orangesRotting( grid=[[2],[1],[1],[1],[2],[1],[1]] )
        self.assertEqual(result, 2)


    def test_case_5(self):

        result = Solution().orangesRotting( grid=[[2],[1],[1],[1],[1],[1],[2],[1],[1]] )
        self.assertEqual(result, 3)



if __name__ == '__main__':

    unittest.main()