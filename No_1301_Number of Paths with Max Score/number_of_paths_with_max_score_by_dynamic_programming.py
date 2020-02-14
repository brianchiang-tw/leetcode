'''

Description:

You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
 

Constraints:

2 <= board.length == board[i].length <= 100

'''

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        
        # modulo constant defined by description
        constant = int( 1e9 ) + 7
        
        # side length of board
        size = len(board)
        
        # a table for highest score path with Dynamic Progrmming
        score = [ [ 0 for y in range(size+1) ] for x in range(size+1) ]
        
        # a talbe for counter of highest score path with Dynamic Progrmming
        count_of_path = [ [ 0 for y in range(size+1) ] for x in range(size+1) ]
        
        # Initialization for start point:
        # Let 
        # score = 0 ( completed in variable declaration )
        # path count = 1
        count_of_path[size-1][size-1] = 1
        
        unreachable = set()
        
        # Update table from start point to end point
        for y in range(size-1, -1, -1):
            for x in range(size-1, -1, -1):
                
                if (y, x) == (size-1, size-1):
                    # start point, table value has been initialized as above.
                    continue
                
                if board[y][x] != 'X' and (y,x) not in unreachable:
                    # find highest score path, excluding obstable
                    
                    # possible candidate:
                    # reach [y][x] from going up, going left, going up-left
                    highest_score = max( score[y+1][x], score[y+1][x+1], score[y][x+1] )
                    
                    if (y, x) == (0, 0):
                        # destination
                        score[y][x] += highest_score
                    else:
                        # in the middle of path finding, update score table
                        score[y][x] += highest_score + int(board[y][x])
                    
                    
                    optimal_count = 0
                    # update path counter with highest score path
                    if highest_score == score[y+1][x]:
                        optimal_count += count_of_path[y+1][x]
                        
                    if highest_score == score[y+1][x+1]:
                        optimal_count += count_of_path[y+1][x+1]
                        
                    if highest_score == score[y][x+1]:
                        optimal_count += count_of_path[y][x+1]
                    
                    count_of_path[y][x] = optimal_count % constant
                
                else:
                    
                    # mark those girds blocked by obstacle 'X' as unreachable
                    if (y,x) not in unreachable:
                        unreachable.add( (y,x) )
                        
                    if (y == size-1 and x >= 1) or ( (y+1,x-1) in unreachable and (y+1,x) in unreachable ):
                        # block by the right hand side 'X' on the last row, or
                        # block by the ┘ shape,  three 'X's on the bottom right
                        unreachable.add( (y,x-1) )
                        
            
        if count_of_path[0][0] == 0:
            # destination is out of reach
            return [0, 0]
        else:
            # destination is reachable
            return [score[0][0], count_of_path[0][0] ]
                       


# n : the side length of board

## Time Complexity: O(n^2)
#
# The overhead in time is the iteration of 2D dynamic programming, which is of ( n^2 ).

## Space Complexity: O(n^2)
#
# The overhead in space is the storage for table, score as well as count_of_path,
# to 2D dynamic programming, which are of O(n^2)



def test_bench():

    test_data = [
                    ["E23","2X2","12S"],
                    ["E12","1X1","21S"],
                    ["E11","XXX","11S"],
                    ["E23","2X2","9XS"]
                ]
    
    # expected output:
    '''
    [7, 1]
    [4, 2]
    [0, 0]
    [7, 1]
    '''

    for board in test_data:

        print( Solution().pathsWithMaxScore(board))
    
    return



if __name__ == '__main__':

    test_bench()