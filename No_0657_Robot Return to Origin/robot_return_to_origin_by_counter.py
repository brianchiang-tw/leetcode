class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        count_of_u, count_of_d, count_of_l, count_of_r = 0, 0, 0, 0
        
        for direction in moves:
            
            if direction == 'U':
                count_of_u += 1
                
            elif direction == 'D':
                count_of_d += 1
            
            elif direction == 'L':
                count_of_l += 1
            
            else:
                count_of_r += 1
                
        
        return count_of_u == count_of_d and count_of_l == count_of_r



# n : the length of moves.

## Time Complexity: O( n )
# 
# The overhead in time is the for loop iterating on direction, which is of O( n )


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and counter, which is of O( 1 )



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