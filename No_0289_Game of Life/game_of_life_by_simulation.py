'''

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]



Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]



Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''


from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        
        
        next_state = [ [ 0 for i in range(cols) ] for j in range(rows) ]
        
        for y in range(rows):
            
            for x in range(cols):
                
                current = board[y][x]
                
                live_neighbor_counter = 0

                
                for offset_y, offset_x in [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0) , (1,1) ]:
                    
                    ny = y + offset_y
                    nx = x + offset_x
                    
                    if rows > ny >= 0 and cols > nx >= 0 :
                        
                        if board[ny][nx] == 1:
                            live_neighbor_counter += 1

                            
                if current:
                    if live_neighbor_counter < 2:
                        # under-population
                        next_state[y][x] = 0

                    
                    elif live_neighbor_counter > 3:
                        # over-population
                        next_state[y][x] = 0

                    else:
                        # keep alive
                        next_state[y][x] = 1
                        
                else: 
                    
                    if live_neighbor_counter == 3:
                        # reproduction
                        next_state[y][x] = 1
        
        
        for y in range(rows):
            for x in range(cols):
                
                board[y][x] = next_state[y][x]



# m : the dimension of rows
# n : the dimension of columns

## Time Complexity: O( m*n )
#
# The overhead in time is the nested loop iterating on (y, x), which is of O( m * n ).


## Space Complexity: O( m*n )
#
# The overhead in space is the storage for board with transition updated, next_state, which is of O( m * n ).




def test_bench():

    test_data = [
                    [
                    [0,1,0],
                    [0,0,1],
                    [1,1,1],
                    [0,0,0]
                    ],

                    [
                    [1,1,1],
                    [0,0,0],
                    [1,1,1],
                    [0,0,0]
                    ]

                ]

    # expected output:
    '''

    [[0, 0, 0], 
    [1, 0, 1], 
    [0, 1, 1], 
    [0, 1, 0]]

    [[0, 1, 0], 
    [0, 0, 0], 
    [0, 1, 0], 
    [0, 1, 0]]

    '''
    
    for test_case in test_data:

        Solution().gameOfLife(test_case)
        print( test_case )
    
    return 



if __name__ == '__main__':

    test_bench()