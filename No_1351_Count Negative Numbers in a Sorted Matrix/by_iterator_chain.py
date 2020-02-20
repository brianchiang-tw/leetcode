from typing import List
from itertools import chain
class Solution:
        
    def countNegatives(self, grid: List[List[int]]) -> int:
                
        return sum( 1 for element in chain( *grid ) if element < 0 )



# m : the dimension of column in matrix
# n : the dimension of row in matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the iteration length of generator expresionn, which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for generator, which is of O( 1 )



def test_bench():

    test_data = [
                    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
                    [[3,2],[1,0]],
                    [[1,-1],[-1,-1]],
                    [[-1]]
                ]

    # expected output:
    '''
    8
    0
    3
    1
    '''


    for matrix in test_data:

        print( Solution().countNegatives(matrix) )
    
    return



if __name__ == '__main__':

    test_bench()