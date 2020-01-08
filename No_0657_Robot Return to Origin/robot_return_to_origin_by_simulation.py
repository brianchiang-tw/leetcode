class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        cur_x, cur_y = 0, 0
        
        for direction in moves:
            
            if direction == 'U':
                cur_y += 1
                
            elif direction == 'D':
                cur_y -= 1
            
            elif direction == 'L':
                cur_x -= 1
            
            else:
                cur_x += 1
                
        
        return (cur_x, cur_y) == (0, 0 )



# n : the length of moves.

## Time Complexity: O( n )
# 
# The overhead in time is the for loop iterating on direction, which is of O( n )


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and coordinates, which is of O( 1 )



def test_bench():

    test_data = ["UD","LL","URDL","UDDU","LRRL"]

    # expected output:
    '''
    True
    False
    True
    True
    True
    '''

    for move_sequence in test_data:

        print( Solution().judgeCircle(move_sequence) )

    return 



if __name__ == '__main__':

    test_bench()