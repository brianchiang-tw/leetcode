'''

Description:

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.

'''



from typing import List
class Solution:
    
    def judge_winner( self, board ):
        
        
        
        for player_token in {'X','O'}:
            
            # check horizontal straight line
            for y in range(3):
                
                if all( [ board[y][x] == player_token for x in range(3) ] ):
                    return player_token
            
            # check vertical straight line
            for x in range(3):
                if all( [ board[y][x] == player_token for y in range(3) ] ):
                    return player_token
                
            
            # check diagnonal line
            if all( [ board[diag][diag] == player_token for diag in range(3) ] ):
                return player_token
            
            # check anti-diagnoal line
            if all( [ board[diag][2-diag] == player_token for diag in range(3) ] ):
                return player_token
        
        
        # if no winner by now, return '='
        return '='
        
        
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        board = [ [ '#' for i in range(3)] for j in range(3) ]
        
        
        turn = 0;
        for one_move in moves:
            
            y, x = one_move
            
            if turn % 2 == 0:
                # A make one move
                board[y][x] = 'X'
                
                
            else:
                # B make one move
                board[y][x] = 'O'
            
            # A and B take turns to play
            turn += 1
            
        winner_token = self.judge_winner( board )
        
        if winner_token == 'X':
            return 'A'
        
        elif winner_token == 'O':
            return 'B'
        
        else:
            if turn ==9:    
                return 'Draw'
            else:
                return 'Pending'



# n : the length of moves

## Time Complexity: O( 1 )
#
# The overhead in time is the for loop iterating one_move, which is of O( 9 ) = O( 1 )


## Space Complexity: O(1)
#
# The overhead in space is the storage for board, which is of O( 3 x 3 ) = O( 9 ) = O( 1 )




def test_bench():

    test_data = [
                    [[0,0],[2,0],[1,1],[2,1],[2,2]],
                    [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]],
                    [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]],
                    [[0,0],[1,1]]
                ]

    # expected output:
    '''
    A
    B
    Draw
    Pending
    '''



    for moves in test_data:

        print( Solution().tictactoe(moves) )

    return 



if __name__ == '__main__':

    test_bench()