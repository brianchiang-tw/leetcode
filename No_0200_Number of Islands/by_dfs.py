'''

Description:

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1



Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''



from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      
        self.h = len(grid)
        
        if self.h == 0:
            # Quick response for empty grid
            return 0
        
        self.w = len( grid[0] )
        
        if self.h * self.w == 1:
            # Quick response for 1x1 grid
            return 1 if grid[0][0] == '1' else 0
        
        # gourp index for island
        self.group_index = 0
        
        
        def dfs( grid, y, x):
            
            if (y < 0) or (x < 0) or (y >= self.h) or (x >= self.w) or (grid[y][x] != '1'):
                return
            
            # mark current position as visited with group index
            grid[y][x] = self.group_index
            
            # visit 4 neighbors in DFS
            dfs( grid, y+1, x)
            dfs( grid, y-1, x)
            dfs( grid, y, x+1)
            dfs( grid, y, x-1)
            
        # -----------------------------------------    
        
        for y in range( self.h ):
            for x in range( self.w ):
                
                # check each position in DFS
                if grid[y][x] == '1':
                    
                    self.group_index -= 1
                    
                    dfs( grid, y, x)
        
        
        return abs( self.group_index )



# m : the height of input grid
# n : the width of input grid

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of nested loop with DFS traversal inside, which is of O( m * n ).

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for DFS recursion call stack, which is of O( m * n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'grid')

def test_bench():

    test_data = [
                    TestEntry( grid =   [
                                            ["1","1","1","1","0"],
                                            ["1","1","0","1","0"],
                                            ["1","1","0","0","0"],
                                            ["0","0","0","0","0"]
                                        ]
                            ),

                    TestEntry( grid =   [
                                            ["1","1","0","0","0"],
                                            ["1","1","0","0","0"],
                                            ["0","0","1","0","0"],
                                            ["0","0","0","1","1"]
                                        ]
                            ),

                    TestEntry( grid =   [
                                            # corner case: 1x1 grid
                                            ["1"],
                                        ]                                        
                            ),

                    TestEntry( grid =   [
                                            # corner case: 1x1 grid
                                            ["0"],
                                        ]       
                            ),

                    TestEntry( grid =   [
                                            # corner case: empty grid
                                        ]       
                            ),


                ]

    # expected output:
    '''
    1
    3
    1
    0
    0
    '''


    for t in test_data:

        print( Solution().numIslands( grid = t.grid) )
    
    return



if __name__ == '__main__':

    test_bench()    