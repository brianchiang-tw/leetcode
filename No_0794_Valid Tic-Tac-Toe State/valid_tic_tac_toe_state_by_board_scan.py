'''

Description:

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.

''' 



from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        rows, cols = [0] *3, [0]*3
        
        first_diag, second_diag = 0, 0
        
        turns = 0
        
        for y in range(3):
            
            for x in range(3):
                
                if board[y][x] == 'O':
                    # 'O' on board[y][x]
                    # 'O' is on the second order of each play
                    turns -= 1
                    
                    # update the existance counter of 'O' of each possible line
                    rows[y] -= 1
                    cols[x] -= 1
                    
                    if y == x:
                        first_diag -= 1
                    
                    if y + x == 2:
                        second_diag -=1
                
                
                elif board[y][x] == 'X':
                    # 'X' on board[y][x]

                    # 'X' is on the first order of each play
                    turns += 1
                    
                    # update the existance counter of 'X' of each possible line
                    rows[y] += 1
                    cols[x] += 1
                    
                    if y == x:
                        first_diag += 1
                        
                    if y + x == 2:
                        second_diag +=1


        # check the win state of 'X'                        
        win_of_x =  rows[0] == 3 or rows[1] == 3 or rows[2] == 3 or \
                    cols[0] == 3 or cols[1] == 3 or cols[2] == 3 or \
                    first_diag == 3 or second_diag == 3
        
        # check the win state of 'O'
        win_of_o =  rows[0] == -3 or rows[1] == -3 or rows[2] == -3 or \
                    cols[0] == -3 or cols[1] == -3 or cols[2] == -3 or \
                    first_diag == -3 or second_diag == -3
        
        
        if ( win_of_x and turns == 0 ) or  ( win_of_o and turns == 1):
            # 'X' must win with first order, and 'O' must win with second order
            return False

        else:
            # 'X' and 'O' must take turns with each other.
            # 'XX' and 'OO' is not allowed.
            return turns == 0 or turns == 1



# m : the dimension of rows, m = 3.
# n : the dimension of columns, n = 3. 

## Time Complexity: O( m * n ) = O( 3 * 3 ) = O( 1 )
#
# The overhead in time is the nested for loops iterating on (y, x), which is of O( 1 )

## Space Complexity: O( m ) = O( n ) = O( 1 )
#
# The overhead in space is the storage for array, rows and cols, which are of O( 1 )

                    
        
def test_bench():

    test_data = [
                    ["O  ", "   ", "   "],
                    ["XOX", " X ", "   "],
                    ["XXX", "   ", "OOO"],
                    ["XOX", "O O", "XOX"]
                ]

    # expected output:
    '''
    False
    False
    False
    True
    '''


    for board_state in test_data:

        print( Solution().validTicTacToe(board_state) )

    return 



if __name__ == '__main__':

    test_bench()
            
            