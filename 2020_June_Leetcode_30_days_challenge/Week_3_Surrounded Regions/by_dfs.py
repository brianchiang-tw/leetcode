'''

Description:

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''



from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        h = len(board)
        w = len(board[0]) if h else 0
        
        if h * w == 0:
            
            # Quick response for empty board
            return
        
        # ---------------------------------------------------------------------------
        
        def dfs( y, x ):
            
            if y < 0 or y >= h or x < 0 or x >= w or board[y][x] != 'O':
                
                # base case and stop condition:
                # current grid is out of boundary or current grid is Not 'O'
                return
            
            
            else:
                
                # current grid is 'O' and is 4-connected to other 'O' cell on border,
                # mark current grid as alive
                board[y][x] = 'alive'

                # visit 4-connected neighbors
                dfs( y-1, x)
                dfs( y+1, x)
                dfs( y, x-1)
                dfs( y, x+1)

        # ---------------------------------------------------------------------------
        
        ## Rescue remaining 'O' cells from other 'O' cells on the border
        
        for y in range(0, h):
            dfs(y, 0)
            dfs(y, w-1)
            
        for x in range(0, w):
            dfs(0, x)
            dfs(h-1, x)
            
        
        
        # 'O' is dead, updated as 'X', if 'O' is not rescued (i.e., 4-connected) by other 'O' cells on border
        transition_table = { 'O': 'X', 'X': 'X', 'alive': 'O'}
        
        for y in range(h):
            for x in range(w):
                
                board[y][x] = transition_table[ board[y][x] ]



# m : the dimension of height of board
# n : the dimension of width of board

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of dfs, which is of o( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the cost of recursion call stack, which is of O( m * n )


import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):
        
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

        Solution().solve( board )
        self.assertEqual( board, 
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]] )


    def test_case_2(self):
        
        board = [["X","O","X","X"],["X","O","X","X"],["X","X","O","X"],["X","O","X","X"]]

        Solution().solve( board )
        self.assertEqual( board, 
[["X","O","X","X"],["X","O","X","X"],["X","X","X","X"],["X","O","X","X"]] )



if __name__ == '__main__':

    unittest.main()
